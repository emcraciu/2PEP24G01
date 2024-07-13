from stocks import Stock
import pandas as pd
import numpy as np
from datetime import datetime
import yfinance as yf
import babel.numbers as bab

import yahoo_data
from decorators import log_time_decorator

class StockAnalytic(Stock):

    # ticker_df = Stock.stock_df

    def __init__(self, val):
        super().__init__(val)

    @staticmethod
    def position_hold_time(date1, date2):
        """ A function that computes the holding time of a stock position in days"""
        if date2 == None:
            date2 = datetime.today().date()
        else:
            date2 = date2
        date_dif = date2 - date1
        return str(date_dif.days) + ' d'

    @staticmethod
    def shares_left(df, ticker):
        dff = df.loc[(df['Stock'] == ticker) & df['sell value'].isnull()]
        if dff.shape[0] > 0:
            stock_tbl = dff
        else:
            stock_tbl = df.loc[(df['Stock'] == ticker) & df['sell value'].notnull()]
        # stock_tbl = df.loc[(df['Stock'] == ticker) & df['sell value'].isnull()]
        stock_tbl = stock_tbl[['Stock', 'nr. shares']]
        nr_shares = stock_tbl.groupby(by=['Stock']).sum()
        return nr_shares.iloc[0][0] #if nr_shares.shape[0] > 0 else 0

    @staticmethod
    @log_time_decorator
    def profit_per_transaction(buy_price, sell_price):
        return np.round(sell_price - buy_price, 2)

    @staticmethod
    @log_time_decorator
    def profit_per_transaction_proc(buy_price, sell_price):
        profit = sell_price - buy_price
        PL_per = np.round(((buy_price + profit) / buy_price - 1) * 100, 2)
        return PL_per

    @staticmethod
    @log_time_decorator
    def profit_per_transaction_now(val, nr_shares, buy_price_per_share, price_now):
        return None if not pd.isnull(val) else np.round(nr_shares * (price_now - buy_price_per_share), 2)

    @staticmethod
    @log_time_decorator
    def profit_per_transaction_now_percent(val, nr_shares, buy_price_per_share, price_now):
        initial_cost = nr_shares * buy_price_per_share
        profit = nr_shares * (price_now - buy_price_per_share)
        return None if not pd.isnull(val) else np.round(((initial_cost + profit) / initial_cost - 1)*100, 2)

    @classmethod
    @log_time_decorator
    def profit_stock(cls, ticker):
        stock_tbl = Stock.stock_df
        # Stock.remove_col(stock_tbl, ['Open (Buy)', 'Close (Sell)', 'nr. shares.1'])
        stock_tbl.insert(stock_tbl.shape[1], 'Profit ($)',
                         stock_tbl.apply(
                             lambda row: StockAnalytic.profit_per_transaction(row['buy value'], row['sell value']),
                             axis=1))
        stock_tbl.insert(stock_tbl.shape[1], 'Profit (%)',
                         stock_tbl.apply(
                             lambda row: StockAnalytic.profit_per_transaction_proc(row['buy value'], row['sell value']),
                             axis=1))
        stock_tbl.insert(stock_tbl.shape[1], 'hold time',
                         stock_tbl.apply(
                             lambda row: StockAnalytic.position_hold_time(row['Buy Date'], row['Sell Date']),
                             axis=1))

        stock_tbl = stock_tbl.loc[stock_tbl['Stock'] == ticker].reset_index(drop=True)
        stock_tbl.index = stock_tbl.index + 1
        return stock_tbl

    @staticmethod
    @log_time_decorator
    def realised_return_stock(df, ticker):
        stock_tbl = df.loc[(df['Stock'] == ticker) & (df['sell value'].notnull())]
        stock_tbl = stock_tbl[['Stock', 'Profit ($)']]
        total_profit = stock_tbl.groupby(by=['Stock']).sum()
        return np.round(total_profit.iloc[0][0], 2) if total_profit.shape[0] > 0 else None

    @staticmethod
    @log_time_decorator
    def realised_return_stock_percent(df, ticker):
        stock_tbl = df.loc[(df['Stock'] == ticker) & (df['sell value'].notnull())]
        stock_tbl = stock_tbl[['Stock', 'buy value', 'sell value']]
        total_profit = stock_tbl.groupby(by=['Stock']).sum()
        res = np.round((total_profit.iloc[0][1]/total_profit.iloc[0][0] - 1) * 100, 2) if total_profit.shape[0] > 0 else None
        return res

    @staticmethod
    @log_time_decorator
    def yahoo_stock_last_price(ticker):
        stock_df = yf.download(ticker, period='5d', progress=False)
        last_price = np.round(stock_df['Adj Close'].tail(1).iloc[0], 2)
        variation = np.round((last_price / stock_df['Adj Close'].tail(2).iloc[0] - 1) * 100, 2)
        return last_price, variation

    @staticmethod
    def value_now(nr_shares, price_now, sell_value):
        return np.round(nr_shares * price_now, 2) if pd.isnull(sell_value) else None

    @staticmethod
    def moneyfmt(val, currency=''):
        return bab.format_currency(val, currency, locale='en_US', decimal_quantization=True)

    @staticmethod
    @log_time_decorator
    def average_cost_per_share(df, ticker):
        dff = df.loc[(df['Stock'] == ticker) & df['sell value'].isnull()]
        if dff.shape[0] > 0:
            stock_tbl = dff
        else:
            stock_tbl = df.loc[(df['Stock'] == ticker) & df['sell value'].notnull()]
        stock_tbl_open = stock_tbl[['Stock', 'buy value']]
        total_cost_open = stock_tbl_open.groupby(by=['Stock']).sum()
        base_cost_open = np.round(total_cost_open.iloc[0][0] / StockAnalytic.shares_left(df, ticker), 2)
        return total_cost_open.iloc[0][0], base_cost_open

    @staticmethod
    @log_time_decorator
    def unrealised_return_stock(df, ticker, price_now):
        dff = df.loc[(df['Stock'] == ticker) & df['sell value'].isnull()]
        if dff.shape[0] > 0:
            value_now = StockAnalytic.shares_left(df, ticker) * price_now
            total_cost = StockAnalytic.average_cost_per_share(df, ticker)[0]
            res = np.round(value_now - total_cost, 2)
        else:
            res = 0
        return res

    @staticmethod
    @log_time_decorator
    def unrealised_return_stock_percent(df, ticker, price_now):
        potential_profit = StockAnalytic.unrealised_return_stock(df, ticker, price_now)
        market_value = StockAnalytic.shares_left(df, ticker) * price_now
        if market_value == 0:
            res = 0
        else:
            res = np.round((market_value / (market_value - potential_profit) - 1) * 100, 2)
        return res if res != 0 else None

    @classmethod
    @log_time_decorator
    def profit_stock_now(cls, ticker):
        df = StockAnalytic.profit_stock(ticker).reset_index(drop=True)
        Stock.remove_col(df, ['Open (Buy)', 'Close (Sell)', 'nr. shares.1'])
        dff = df.loc[(df['Stock'] == ticker) & df['sell value'].isnull()]
        price_now = StockAnalytic.yahoo_stock_last_price(ticker)[0]

        df.insert(df.shape[1] - 3, 'value now',
                   df.apply(
                       lambda row: StockAnalytic.value_now(row['nr. shares'], price_now, row['sell value']), axis=1))
        df.insert(df.shape[1] - 1, 'P/L ($)',
                         df.apply(
                             lambda row: StockAnalytic.profit_per_transaction_now(row['sell value'], row['nr. shares'],
                                                                    row['price/share'], price_now), axis=1))
        df.insert(df.shape[1] - 1, 'P/L (%)',
                   df.apply(
                       lambda row: StockAnalytic.profit_per_transaction_now_percent(row['sell value'], row['nr. shares'],
                                                                    row['price/share'], price_now), axis=1))
        # df.loc[df.shape[0]] = ['' for i in range(df.shape[1])]
        totals = ['Totals', StockAnalytic.shares_left(Stock.stock_df, ticker),
                  StockAnalytic.average_cost_per_share(Stock.stock_df, ticker)[1],
                  StockAnalytic.average_cost_per_share(Stock.stock_df, ticker)[0], None, None, None, None,
                  np.round((StockAnalytic.shares_left(Stock.stock_df, ticker) if dff.shape[0] > 0 else 0) * price_now, 2),
                  StockAnalytic.realised_return_stock(Stock.stock_df, ticker),
                  StockAnalytic.realised_return_stock_percent(Stock.stock_df, ticker),
                  np.round(StockAnalytic.shares_left(Stock.stock_df, ticker) * price_now, 2) - \
                  StockAnalytic.average_cost_per_share(Stock.stock_df, ticker)[0] if dff.shape[0] > 0 else None,
                  StockAnalytic.unrealised_return_stock_percent(df, ticker, price_now), None]
        df.loc[df.shape[0]] = totals
        df.index = df.index + 1

        m = df.shape[0]
        n = m if m <= 12 else 12

        return df#.iloc[(m - n):m, :]

    @staticmethod
    @log_time_decorator
    def stock_weight(df, ticker):
        dff = Stock.stock_df.loc[(Stock.stock_df['Stock'] == ticker) & Stock.stock_df['sell value'].isnull()]
        df1 = Stock.stock_df
        ticker_open = df1.loc[df1['Close (Sell)'] != 'S']['Stock'].unique()
        if dff.shape[0] > 0:
            cost = StockAnalytic.average_cost_per_share(Stock.stock_df, ticker)[0]
            df = df[df.Stock.isin(list(ticker_open))]
            total_cost = df['Cost ($)'].sum()
            res = np.round((cost/total_cost) * 100, 2)
        else:
            res = None
        return res

    @staticmethod
    @log_time_decorator
    def stock_weight_now(df, ticker):
        dff = Stock.stock_df.loc[(Stock.stock_df['Stock'] == ticker) & Stock.stock_df['sell value'].isnull()]
        df1 = Stock.stock_df
        ticker_open = df1.loc[df1['Close (Sell)'] != 'S']['Stock'].unique()
        if dff.shape[0] > 0:
            value_now_stock = np.round(StockAnalytic.shares_left(Stock.stock_df, ticker) * \
                                       StockAnalytic.yahoo_stock_last_price(ticker)[0], 2)
            df = df[df.Stock.isin(list(ticker_open))]
            value_now_total = df['Market Cap ($)'].sum()
            res = np.round((value_now_stock / value_now_total) * 100, 2)
        else:
            res = None
        return res

    @classmethod
    @log_time_decorator
    def portfolio_summary(cls, ticker_lst, ticker_open):
        df = pd.DataFrame({'Stock': ticker_lst}, index=np.arange(len(ticker_lst)))
        # with open(r'C:\Users\Ciprian QCD\PycharmProjects\2PEP24G01_me\homework\ciprian\StockApp\test.txt', 'w') as f:
        #     f.write(str(list(ticker_lst)))

        current_prices = yahoo_data.yahoo_data(list(ticker_lst))[0]
        current_chg = yahoo_data.yahoo_data(list(ticker_lst))[1]

        # with open(r'C:\Users\Ciprian QCD\PycharmProjects\2PEP24G01_me\homework\ciprian\StockApp\test.txt', 'a') as f:
        #     f.write(str(current_chg))

        # current_prices = {}
        # current_chg = {}
        # for ticker in ticker_lst:
        #     current_prices[ticker] = StockAnalytic.yahoo_stock_last_price(ticker)[0]
        #     current_chg[ticker] = StockAnalytic.yahoo_stock_last_price(ticker)[1]

        df.insert(df.shape[1], 'shares left',
                  df.apply(lambda row: StockAnalytic.shares_left(Stock.stock_df, row['Stock']), axis=1))
        df.insert(df.shape[1], 'Cost ($)',
                  df.apply(lambda row: StockAnalytic.average_cost_per_share(Stock.stock_df, row['Stock'])[0], axis=1))
        df.insert(df.shape[1], 'W buy (%)',
                  df.apply(lambda row: StockAnalytic.stock_weight(df, row['Stock']), axis=1))
        df.insert(df.shape[1], 'Market Cap ($)',
                  df.apply(lambda row: np.round(current_prices[row['Stock']] * \
                                       StockAnalytic.shares_left(Stock.stock_df, row['Stock']), 2)
                           if row['Stock'] in ticker_open else None, axis=1))
        df.insert(df.shape[1], 'W now (%)',
                  df.apply(lambda row: StockAnalytic.stock_weight_now(df, row['Stock']), axis=1))
        df.insert(df.shape[1], 'Profit ($)',
                  df.apply(lambda row: StockAnalytic.realised_return_stock(Stock.stock_df, row['Stock']), axis=1))
        df.insert(df.shape[1], 'Profit (%)',
                  df.apply(lambda row: StockAnalytic.realised_return_stock_percent(Stock.stock_df, row['Stock']), axis=1))
        df.insert(df.shape[1], 'P/L ($)',
                  df.apply(lambda row: StockAnalytic.unrealised_return_stock(Stock.stock_df, row['Stock'],
                                        current_prices[row['Stock']]) if row['Stock'] in ticker_open else None, axis=1))
        df.insert(df.shape[1], 'P/L (%)',
                  df.apply(lambda row: StockAnalytic.unrealised_return_stock_percent(Stock.stock_df, row['Stock'],
                                        current_prices[row['Stock']]) if row['Stock'] in ticker_open else None, axis=1))
        df.insert(df.shape[1], 'Last Price',
                  df.apply(lambda row: StockAnalytic.moneyfmt(current_prices[row['Stock']], 'USD'), axis=1))
        df.insert(df.shape[1], 'Chg %',
                  df.apply(lambda row: str(current_chg[row['Stock']]) + ' %', axis=1))

        df = df.sort_values(by='P/L ($)', ascending=False).reset_index(drop=True)
        try:
            PL = np.round((df['Market Cap ($)'].sum() / (df['Market Cap ($)'].sum() - df['P/L ($)'].sum()) - 1) * \
                         100, 2)
        except ZeroDivisionError:
            PL = None
        profits = ['Totals', None, df['Cost ($)'].sum(), None, df['Market Cap ($)'].sum(), None,
                   df['Profit ($)'].sum(), None, df['P/L ($)'].sum(),
                   PL , None, None]
        df.loc[df.shape[0]] = profits
        df.index = df.index + 1

        return df





