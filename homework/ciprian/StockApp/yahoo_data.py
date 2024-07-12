import yfinance as yf
import numpy as np
from decorators import log_time_decorator

@log_time_decorator
def yahoo_stock_last_price(ticker):
    stock_df = yf.download(ticker, period='5d', progress=False)
    last_price = np.round(stock_df['Adj Close'].tail(1).iloc[0], 2)
    variation = np.round((last_price / stock_df['Adj Close'].tail(2).iloc[0] - 1) * 100, 2)
    return last_price, variation

@log_time_decorator
def yahoo_data(tickers):
    if type(tickers) == str:
        return yahoo_stock_last_price(tickers)
    else:
        current_prices1 = {}
        current_chg1 = {}
        yahoo_results = yahoo_stock_last_price(tickers)
        for ticker in tickers:
            current_prices1[ticker] = yahoo_results[0].loc[ticker]
            current_chg1[ticker] = yahoo_results[1].loc[ticker]
        return current_prices1, current_chg1

