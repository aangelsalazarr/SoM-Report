import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
import seaborn as sns
from scipy import stats

# industrial metals list
lead = 0
zinc = 0
tin = 0
aluminum = 0
aluminiumAlloy = 0
lmeNi = 0
cobalt = 0
molybdenum = 0

# precious metals list
gold = 0
platinum = 0
palladium = 0
silver = 0

# energy related metals not already covered list
lithium = 0
graphite = 0
chromium = 0
silicon = 0
manganese = 0

# **************************COPPER**********************************************

# creating a variable that is the copper index in
lmeCu = yf.Ticker("HG=F")

# topics of interest that are available for data sourcing
topics = {
    'exchange', 'shortName', 'underlyingSymbol', 'previousClose',
    'regularMarketOpen', 'twoHundredDayAverage', 'regularMarketDayHigh',
    'averageDailyVolume10Day', 'regularMarketPreviousClose',
    'fiftyDayAverage', 'open', 'averageVolume10days', 'expireDate',
    'regularMarketDayLow', 'regularMarketVolume', 'openInterest',
    'averageVolume', 'dayLow', 'ask', 'askSize', 'volume', 'fiftyTwoWeekHigh',
    'fiftyTwoWeekLow', 'bid', 'bidSize', 'dayHigh', 'regularMarketPrice'
}

# storing a dictionary on historic info related to copper
cu_history = lmeCu.history(period='1Y')

# converting index to columns
cu_history.reset_index(inplace=True)

# dropping dividens and strock split columns because NA
cu_history.drop(['Dividends', 'Stock Splits'], inplace=True, axis=1)

'''
Let's now plot historic data.
Historic data contains the following columns
- date (index), open, high, low, close, volume, dividends, stock splits
'''

# defining dimensions of subplots & aesthetics
sns.set_style('white')

# create a chart in each subplot
sns.lineplot(data=cu_history, x='Date', y='Open', color='green')
ax2 = plt.twinx()
sns.lineplot(data=cu_history, x='Date', y='Volume', color='lightgreen', ax=ax2)

plt.show()

# **************************COPPER**********************************************
