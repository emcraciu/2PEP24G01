import csv
import json
import warnings
warnings.filterwarnings("ignore")
import streamlit as st
import streamlit_authenticator as stauth
import requests

from stocks import Stock
from stocks_analytics import StockAnalytic
import config_data

def main() -> None:
    # with open(r'C:\Users\Ciprian QCD\PycharmProjects\2PEP24G01_me\homework\ciprian\StockApp\config.yaml') as file:
    #     config = yaml.load(file, Loader=SafeLoader)

    config = config_data.Users(), config_data.Cookies(), config_data.Preauthorized()
    authenticator = stauth.Authenticate(
        config[0]['credentials'],
        config[1]['cookie'].get('csporea', {}).get('name', 'user_name'),
        config[1]['cookie'].get('csporea', {}).get('key', 'user_key'),
        config[1]['cookie'].get('csporea', {}).get('expiry_days', 30),
        config[2]['pre-authorized']
    )
    authenticator.login()

    if st.session_state["authentication_status"]:
        authenticator.logout('Logout')
        st.write(f'Welcome *{st.session_state["name"]}*')

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

        # current_ticker_price = {}
        # current_ticker_chg = {}
        # stock_name = list(ticker_dict['Stocks with open positions'])
        # yahoo_results = StockAnalytic.yahoo_stock_last_price(stock_name)
        # for ticker in stock_name:
        #     current_ticker_price[ticker] = yahoo_results[0].loc[ticker]
        #     current_ticker_chg[ticker] = yahoo_results[1].loc[ticker]

        col1, col2, col3, col4, col5 = st.columns([0.75, 0.1, 0.75, 0.3, 1])

        try:
            ticker_lst = col1.selectbox('Choose Ticker Symbol List', ticker_dict.keys(),
                                        help='Filter report to show only a selection of Stock')

            with open(r'C:\Users\Ciprian QCD\PycharmProjects\2PEP24G01_me\homework\ciprian\StockApp\valid_tickers.csv',
                      'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(ticker_dict[ticker_lst])

            ticker = col3.selectbox('Choose Ticker Symbol', ticker_dict[ticker_lst],
                                    help='Filter report to show only one Stock')

            trigger_value = col4.selectbox('trigger (%)', [1,2,5,7,10,15],
                                        help='chose a &value for stop loss or take profit')

            response = requests.get(r"http://127.0.0.1:5000//")
            text = response.text
            price = json.loads(text)
            if price[1][ticker] < -trigger_value:
                col5.error(f"Stop Loss for {ticker} activated. Price decreased by: {price[1][ticker]} %")
            elif price[1][ticker] > trigger_value:
                col5.success(f"Take Profit for {ticker} activated. Price increased by: {price[1][ticker]} %")

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

        except (ValueError, KeyError, AttributeError):
            pass

    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')


if __name__ == "__main__":
    st.set_page_config(page_title='Stock Porfolio Analytics and Management',
                    page_icon=':bar_chart:', layout='wide')

    main()

