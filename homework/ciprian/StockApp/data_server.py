from flask import Flask
import pandas as pd

import yahoo_data
from decorators import log_time_decorator

app = Flask(__name__)
@app.route('/')
@log_time_decorator
def server_price_data():
    ticker_df = pd.read_csv(r'C:\Users\Ciprian QCD\PycharmProjects\2PEP24G01_me\homework\ciprian\StockApp\valid_tickers.csv')
    ticker_list = list(ticker_df.columns)
    # ticker_list = ['TSLA', 'TIGR']
    res = yahoo_data.yahoo_data(ticker_list)
    return list(res)



if __name__ == '__main__':
    app.run(debug=True)