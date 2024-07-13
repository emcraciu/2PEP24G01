import csv

import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.shared import JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder

from stocks import Stock
from stocks_analytics import StockAnalytic
import yfinance as yf
import cufflinks as cf
import datetime as dt

import streamlit_authenticator as stauth
from homework.ciprian.StockApp import config_data


@st.cache_data
def clean_data(df):
    df = df.copy()
    df.columns = df.columns.str.lower().str.replace(" ", "_", regex=False).str.replace("._", "_", regex=False)
    df.columns = df.columns.str.lower().str.replace("/", "_", regex=False).str.replace("(", "", regex=False).str.replace(")", "", regex=False)
    return df

def user_input(msg: str, opt: int):
    if opt == 1:
        val = st.number_input(msg, 0, 100)
    elif opt == 2:
        val = st.text_input(msg)
    else:
        val = None
    return val


def main() -> None:

    config = config_data.Users(), config_data.Cookies(), config_data.Preauthorized()
    authenticator = stauth.Authenticate(
        config[0]['credentials'],
        config[1]['cookie']['csporea']['name'],
        config[1]['cookie']['csporea']['key'],
        config[1]['cookie']['csporea']['expiry_days'],
        config[2]['pre-authorized']
    )
    authenticator.login()

    if st.session_state["authentication_status"]:
        authenticator.logout()
        st.write(f'Welcome *{st.session_state["name"]}*')

        st.header("Stocks Analytics :bar_chart:")
        # st.markdown("# Stocks Analytics")
        st.sidebar.markdown("# Stocks Analytics")


        uploaded_data = st.sidebar.file_uploader(
            "Drag and Drop or Click to Upload", type=".csv", accept_multiple_files=False)
        tranz_df = Stock.load_data(uploaded_data)

        with st.expander("View your data as a Dataframe"):
            st.write(tranz_df)

        Stock.add_col(tranz_df, 'Date', 'Buy Date', 5)
        Stock.add_col(tranz_df, 'Date.1', 'Sell Date', tranz_df.shape[1])
        Stock.remove_col(tranz_df, ['Date', 'Date.1', 'col1', 'buy_date_new'])

        ticker_dict = {'Stocks with open positions': Stock.tickers()[1],
                       'Stocks no longer hold': Stock.tickers()[2],
                       'All Stocks transactions': Stock.tickers()[0] }

        col1, col2, col3, col4, col5 = st.columns([0.75, 0.1, 0.75, 0.1, 0.75])
        ticker_lst = col1.selectbox('Choose Ticker Symbol List', ticker_dict.keys(), help='Filter report to show only one Stock')

        with open(r'C:\Users\Ciprian QCD\PycharmProjects\2PEP24G01_me\homework\ciprian\StockApp\valid_tickers.csv',
                  'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(ticker_dict[ticker_lst])

        ticker = col3.selectbox('Choose Ticker Symbol', ticker_dict[ticker_lst], help='Filter report to show only one Stock')

        options_lst = ['only open transactions', 'only closed transactions', 'all transactions']
        tbl_options = col5.selectbox('Table view options', options_lst,
                                      help='Filter table to show only open, closed or all transactions')

        col1a, col2a, col3a = st.columns([1,2,2])

        try:
            user_ticker = col1a.text_input('Input a ticker stock symbol: ')
            ticker = ticker if user_ticker == '' else user_ticker.upper()

            tranz_df = StockAnalytic.profit_stock_now(ticker)
            if tbl_options == options_lst[0]:
                tranz_df = tranz_df[tranz_df['sell value'].isnull() ]
            elif tbl_options == options_lst[1]:
                tranz_df1 = tranz_df[tranz_df['sell value'].notnull() ]
                tranz_df = pd.concat([tranz_df1, tranz_df.iloc[-1:]])
            elif tbl_options == options_lst[2]:
                tranz_df = tranz_df

            Stock.remove_col(tranz_df, ['Buy Date', 'Sell Date'])

            # Defining Table esthetics parameters for java script
            cellsytle_jscode = JsCode(
                """
            function(params) {
                if (params.value > 0) {
                    return {
                        'color': '#00A86B',
                    }
                } else if (params.value < 0) {
                    return {
                        'color': 'red',
                    }
                } else {
                    return {
                        'color': 'white',
                    }
                }
            };
            """
            )

            try:
                st.subheader(f'Value of selected Stock: {ticker}')
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

                gb = GridOptionsBuilder.from_dataframe(tranz_df)
                gb.configure_columns(
                    ('Profit ($)', 'Profit (%)', 'P/L ($)', 'P/L (%)', ),
                    cellStyle=cellsytle_jscode,
                )
                gb.configure_pagination()
                gb.configure_columns(("Stock"), pinned=True)
                gb.configure_selection("single")
                gridOptions = gb.build()

                AgGrid(tranz_df, gridOptions=gridOptions, allow_unsafe_jscode=True, fit_columns_on_grid_load=True)
            except KeyError:
                pass

            tickerData = yf.Ticker(ticker)
            tickerDf = tickerData.history(period='1d',
                                          start=dt.date.today() - dt.timedelta(days=90), end=dt.date.today())

            with st.expander(f'View price chart for: {ticker} '):
                st.subheader('**Stock price evolution from yahoo Finance**')
                qf = cf.QuantFig(tickerDf, title=f'candle price chart for: {ticker} ', name=ticker, legend='top')
                qf.add_bollinger_bands()
                qf.add_rsi()
                fig = qf.iplot(asFigure=True)
                st.plotly_chart(fig)


            portfolio_summary_df = StockAnalytic.portfolio_summary(ticker_dict[ticker_lst], ticker_dict['Stocks with open positions'])

            st.subheader('Value of Portfolio Account')
            totals_card = portfolio_summary_df.iloc[-1:].groupby('Stock', as_index=False).sum()
            try:
                st.metric(
                    "Total of Portfolio",
                    f"${totals_card['Market Cap ($)'].sum():.2f}",
                    f"{totals_card['P/L ($)'].sum():.2f} $ {totals_card['P/L (%)'].sum():.2f} %",
                )
            except KeyError:
                pass


            gb = GridOptionsBuilder.from_dataframe(portfolio_summary_df)
            gb.configure_columns(
                ('Profit ($)', 'Profit (%)', 'P/L ($)', 'P/L (%)',),
                cellStyle=cellsytle_jscode,
            )
            gb.configure_pagination()
            gb.configure_columns(("Stock"), pinned=True)
            gb.configure_selection("single")
            gridOptions = gb.build()

            with st.expander("View Portfolio Summary"):
                AgGrid(portfolio_summary_df, gridOptions=gridOptions, allow_unsafe_jscode=True, fit_columns_on_grid_load=True)
        except ValueError:
            pass

    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')



if __name__ == "__main__":
    st.set_page_config(page_title='Stock Porfolio Analytics and Management',
                       page_icon=':bar_chart:', layout='wide')

    main()