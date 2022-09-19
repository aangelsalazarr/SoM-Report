import pandas as pd
import seaborn as sns
import os
import yfinance as yf
import matplotlib.pyplot as plt
import dataframe_image as dfi
from pdfConverter import save_multi_image
from matplotlib import rc

rc('mathtext', default='regular')
plt.rcParams["figure.autolayout"] = True
pd.set_option('display.max_columns', None)

'''
The purpose of this file is to grab data related to the top 5 cryptocurrencies
and create visualizations that are helpful in getting a sense of what is going
on. Looking at the following cryptos:
1. Bitcoin
2. Ethereum
3. Tether
4. USD Coin
5. BNB

We would also like to compare the 5 to other indexes in the market and sector
'''

cryptoList = ['BTC-USD', 'ETH-USD', 'USDT-USD', 'USDC-USD', 'BNB-USD']

# create a empty dataframe
appendedData = pd.DataFrame(columns=['Ticker'])

# what we want to grab from info
topics = {'shortName'}

# process to grab historical data
for crypto in cryptoList:
    a = yf.Ticker(str(crypto)).history(period="3Y")  # how many years of data
    a.drop(['Dividends', 'Stock Splits'], inplace=True, axis=1)
    a = a.assign(Delta=a['Close'].pct_change())
    # info = yf.Ticker(str(index)).info
    #filterInfo = {key: info[key] for key in info.keys() & topics}
    #filterInfo = pd.DataFrame(filterInfo, index=[0, ])
    appendedData = pd.concat([appendedData, pd.DataFrame(a)])
    #appendedData = pd.concat([appendedData, filterInfo])
    if appendedData['Ticker'].isnull:
        appendedData['Ticker'].fillna(crypto, inplace=True)
    else:
        continue


# resetting our index
appendedData.reset_index(inplace=True)

# renaming the column holding date values
appendedData.rename(columns={'index':'Date'}, inplace=True)

# converting our date column to a date value
appendedData['Date'] = pd.to_datetime(appendedData['Date'])

# checkin our df
print(appendedData)

