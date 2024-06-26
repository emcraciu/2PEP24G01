import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class Stock():

    stock_df = None

    def __init__(self, val):
        self.val = val

    @classmethod
    def load_data(cls, uploaded_data):
        if uploaded_data is None:
            st.info("Plese select a file to upload your data")
            uploaded_data = pd.DataFrame(
                columns=['Stock', 'Open (Buy)', 'nr. shares', 'price/share', 'buy value', 'Date', 'Close (Sell)',
                         'nr. shares.1', 'price/share.1', 'sell value', 'Date.1', 'col1', 'buy_date_new'])
            tranz_df = uploaded_data
            # tranz_df = pd.read_csv('./Rev - data_new.csv')
            cls.stock_df = tranz_df
        else:
            tranz_df = pd.read_csv(uploaded_data)
            tranz_df['Stock'].mask(tranz_df['Stock'] == 'FB', 'META', inplace = True)
            cls.stock_df = tranz_df
            msg = st.sidebar.success("File succesfully uploaded!")
            # time.sleep(3)
            # msg.empty()
        return tranz_df


    @staticmethod
    # A function that formats the Date columns into python datetime format
    def format_date(strDate):
        if type(strDate) == str:
            strDate = strDate.strip()
            date = datetime.strptime(strDate, '%d.%m.%Y').date()
        else:
            date = None
        return date

    @staticmethod
    def add_col(df, col_name, new_col_name, insert_after_col):
        return df.insert(insert_after_col, new_col_name, df.apply(lambda row: Stock.format_date(row[col_name]), axis=1))

    @staticmethod
    def remove_col(df, col_lst):
        return df.drop(col_lst, axis=1, inplace=True)

    @classmethod
    def ticker_all(cls):
        return Stock.stock_df['Stock'].unique()

    @classmethod
    def tickers(cls):
        df = Stock.stock_df
        ticker_delisted = ['HOME', 'REGI']
        ticker_all = np.setdiff1d(df['Stock'].unique(), ticker_delisted)
        ticker_open = df.loc[df['Close (Sell)'] != 'S']['Stock'].unique()
        ticker_closed = np.setdiff1d(np.setdiff1d(ticker_all, ticker_open), ticker_delisted)
        return ticker_all, ticker_open, ticker_closed

