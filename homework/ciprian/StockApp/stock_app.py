import streamlit as st

from stocks import Stock
from stocks_analytics import StockAnalytic



def main() -> None:
    st.header("Stock Porfolio Analytics and Management")
    # st.markdown("# Main page")
    # st.sidebar.markdown("# Main page")


    st.sidebar.subheader("Upload your CSV from your Broker Account")
    uploaded_data = st.sidebar.file_uploader(
        "Drag and Drop or Click to Upload", type=".csv", accept_multiple_files=False)

    tranz_df = Stock.load_data(uploaded_data)

    Stock.add_col(tranz_df, 'Date', 'Buy Date', 5)
    Stock.add_col(tranz_df, 'Date.1', 'Sell Date', tranz_df.shape[1])
    Stock.remove_col(tranz_df, ['Date', 'Date.1', 'col1', 'buy_date_new'])

    ticker_dict = {'Stocks with open positions': Stock.tickers()[1],
                   'Stocks no longer hold': Stock.tickers()[2],
                   'All Stocks transactions': Stock.tickers()[0]}

    col1, col2, col3, col4 = st.columns([0.75, 0.1, 0.75, 1])

    try:
        ticker_lst = col1.selectbox('Choose Ticker Symbol List', ticker_dict.keys(), help='Filter report to show only one Stock')

        ticker = col3.selectbox('Choose Ticker Symbol', ticker_dict[ticker_lst], help='Filter report to show only one Stock')

        tranz_df = StockAnalytic.profit_stock_now(ticker)
        Stock.remove_col(tranz_df, ['Buy Date', 'Sell Date'])

        portfolio_summary_df = StockAnalytic.portfolio_summary(ticker_dict[ticker_lst],
                                                               ticker_dict['Stocks with open positions'])
        st.subheader('Value of Portfolio Account')
        totals_card = portfolio_summary_df.iloc[-1:].groupby('Stock', as_index=False).sum()
        st.metric(
            "Total of Portfolio",
            f"${totals_card['Market Cap ($)'].sum():.2f}",
            f"{totals_card['P/L ($)'].sum():.2f} $ {totals_card['P/L (%)'].sum():.2f} %",
        )

        st.subheader(f'Value of Stock: {ticker}')
        totals = tranz_df.iloc[-1:].groupby('Stock', as_index=False).sum()
        col1b, col2b = st.columns([2, 2])
        col1b.metric(
            f"Total of All Open positions",
            f"${totals['value now'].sum():.2f}",
            f"{totals['P/L ($)'].sum():.2f} $ {totals['P/L (%)'].sum():.2f} %",
        )
        col2b.metric(
            "Last Price",
            f'${StockAnalytic.yahoo_stock_last_price(ticker)[0]}',
            f'{StockAnalytic.yahoo_stock_last_price(ticker)[1]} %'
        )

    except ValueError:
        pass
    except KeyError:
        pass




if __name__ == "__main__":
    st.set_page_config(page_title='Stock Porfolio Analytics and Management',
    				page_icon=':bar_chart:', layout='wide')

    main()