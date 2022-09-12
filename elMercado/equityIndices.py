import pandas as pd
import seaborn as sns
import os
import yfinance as yf
pd.set_option('display.max_columns', None)

'''
The purpose of this file is to grab all relevant data on equity indices. The 
following will be tracked along with date data type:
- s&p 500 index
- nasdaq composite index
- russell 1000 index
- russell 1000 value index
- russell 1000 growth index
- russell 2000 index
- russell 2000 value index
- russell 2000 growth index
'''

# want to initialize  multiple ticker objects
tickersList = '^SPX ^IXIC ^RUI ^RLV ^RLG ^RUT ^RUJ ^RUO'
tickers = yf.Tickers(tickersList)

# access all of the datas historical data
equityIndicesHistData = tickers.history()

# cleaning up our data
equityIndicesHistData.reset_index(inplace=True)
equityIndicesHistData.drop(['Dividends', 'Stock Splits', 'Volume'],
                           inplace = True, axis=1)

print(equityIndicesHistData)
