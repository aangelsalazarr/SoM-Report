# purpose of this file is to provide benchmark values on financial markets
import yfinance as yf
import pandas as pd

# equity indices
sp500_index = yf.Ticker("^SPX")
sp500_dict = sp500_index.info  # this is a dictionary

# purpose is to extract specific key value pairs that we care about
filtered_sp500_dict = {key: sp500_dict[key] for key in sp500_dict.keys() & {
    'shortName', 'previousClose', 'regularMarketOpen',
    'twoHundredDayAverage', 'beta', 'fiftyTwoWeekHigh',
    'regularMarketPreviousClose'}}

# converting dicionary into df
sp500_df = pd.DataFrame(filtered_sp500_dict, index=['i', ])
print(sp500_df.head())

# fixed income / credit

# real assets

# volatility

# fixed income yield

# foreign exchange

# commodities

# consumer price index
