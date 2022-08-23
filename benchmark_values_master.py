# purpose of this file is to provide benchmark values on financial markets
import yfinance as yf
import pandas as pd

# equity indices
sp500_index = yf.Ticker("^SPX")
sp500_dict = sp500_index.info # this is a dictionary

# we would like to grab a list of all keys
for key, value in sp500_dict.items():
    pass # printing nothing because we do not need this at moment

# purpose is to extract specific key value pairs that we care about
filtered_sp500 = {key: sp500_dict[key] for key in sp500_dict.keys() & {
    'shortName', 'previousClose', 'regularMarketOpen',
    'twoHundredDayAverage', 'beta', 'fiftyTwoWeekHigh',
    'regularMarketPreviousClose'}}

# showing our filtered data
print("filtered sp500 information: " + str(filtered_sp500))


# fixed income / credit

# real assets

# volatility

# fixed income yield

# foreign exchange

# commodities

# consumer price index

