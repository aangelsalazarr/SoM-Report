# purpose is to gather data related to volatility and print our a plot
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import matplotlib.dates as mdates
import numpy as np
import os
import requests
import json
import datetime
from bls_data_processor import fetch_bls_series
# finding ticker symbol for volatility on yfinance
volatility_index = yf.Ticker("^VIX")
# converting information on vix --> dictionary
vix_dict = volatility_index.info
# getting historical market data
hist_data = volatility_index.history(period='1Y')

# now we will be filtering out to only data that we need into a df
filtered_vix = {key: vix_dict[key] for key in vix_dict.keys() & {
    'shortName', 'symbol', 'previousClose', 'regularMarketOpen',
    'twoHundredDayAverage', 'regularMarketPreviousClose', 'fiftyDayAverage',
    'open', 'fiftyTwoWeekHigh', 'fiftyTwoWeekLow', 'regularMarketPrice'
}}

# converting our filtered dictionary into a df
vix_df = pd.DataFrame(filtered_vix, index = [0, ])
vix_df = vix_df.sort_index(axis=1)

# adding col of percent change of index
vix_df = vix_df.assign(percentChange = (vix_df['regularMarketOpen'] - vix_df[
    'regularMarketPreviousClose']) / vix_df['regularMarketPreviousClose']*100)

# plotting the percent change
# vix_df.plot(x='shortName', y='percentChange', kind='bar')

# adding a percent change col to historical data df
hist_data = hist_data.assign(percentChange = hist_data['Open'].pct_change())

# please note that historical data is already a df so we can plot it
ax1 = plt.subplot()
l1, = ax1.plot(hist_data['Open'], color='blue')
ax1.set_ylabel('VIX Index Value')
ax2 = ax1.twinx()
ax2.set_ylabel('% Change VIX')
l2, = ax2.plot(hist_data['percentChange'], color='pink', alpha=0.5)
plt.legend([l1, l2], ['VIX Value', '% Change'])
plt.title("CBOE Volatility Index")
# plt.show()

# ______________________________________________________________________________
# BLS API DATA FROM HERE AND DOWN
# grabbing data from bls public api
# we want to grab the bls from our virtual environment
bls_api_key = os.environ.get('blsAPI')

# series id of interest
unemployment_rate = "LNS14000000"
cpi = "CUUR0000SA0" # consumer price index
eci = "CIU1010000000000A" # employment cost index
imports = "EIUIR" # imports all commodities
exports = "EIUIQ" # exports, all commodities

# setting up our series list
series = [unemployment_rate, cpi, eci, imports, exports]
end_year = datetime.datetime.now().year
start_year = end_year - 5

# grabbing bls api data
bls_data = fetch_bls_series(series, startyear=start_year, endyear=end_year,
                            registrationKey=bls_api_key)
print(json.dumps(bls_data, indent=2))
