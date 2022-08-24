# purpose is to gather data related to volatility and print our a plot
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import matplotlib.dates as mdates
import numpy as np

# finding ticker symbol for volatility on yfinance
volatility_index = yf.Ticker("^VIX")
# converting information on vix --> dictionary
vix_dict = volatility_index.info
# getting historical market data
historical_data = volatility_index.history(period='1Y')

# now we will be filtering out to only data that we need into a df
filtered_vix = {key: vix_dict[key] for key in vix_dict.keys() & {
    'shortName', 'symbol', 'previousClose', 'regularMarketOpen',
    'twoHundredDayAverage', 'regularMarketPreviousClose', 'fiftyDayAverage',
    'open', 'fiftyTwoWeekHigh', 'fiftyTwoWeekLow', 'regularMarketPrice'
}}

# converting our filtered dictionary into a df
vix_df = pd.DataFrame(filtered_vix, index = [0, ])
vix_df = vix_df.sort_index(axis=1)

# please note that historical data is already a df so we can plot it
# converting our date col into date type

historical_data.plot(y='Open')
plt.title("CBOE Volatility Index")
plt.xlabel("Date")
plt.ylabel("Open")
plt.show()
