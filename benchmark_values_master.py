# purpose of this file is to provide benchmark values on financial markets
import yfinance as yf
import pandas as pd

# sp500 index
sp500_index = yf.Ticker("^SPX")
sp500_dict = sp500_index.info

# purpose is to extract specific key value pairs that we care about
filtered_sp500_dict = {key: sp500_dict[key] for key in sp500_dict.keys() & {
    'shortName', 'regularMarketOpen',
    'twoHundredDayAverage', 'fiftyTwoWeekHigh',
    'regularMarketPreviousClose'}}

# converting dicionary into df
sp500_df = pd.DataFrame(filtered_sp500_dict, index=['i', ])
sp500_df = sp500_df.sort_index(axis=1)
# print(sp500_df.head())

# now we want to do this with various entities not only the sp500
# equity indices
equity_indices = ['^SPX', '^IXIC', '^RUI', '^RLV', '^RLG', '^RUT', '^RUJ',
                                                                   '^RUO']

# for each ticker symbol, let's first filter out
index_value = 0

for index in equity_indices:
    a = yf.Ticker(str(index)).info
    filtered_a = {key: a[key] for key in a.keys() & {
        'shortName', 'regularMarketOpen',
        'twoHundredDayAverage', 'fiftyTwoWeekHigh',
        'regularMarketPreviousClose'
    }}
    df = pd.DataFrame(filtered_a, index=[str(index_value + 1), ])
    df = df.sort_index(axis=1)
    print(df)

# fixed income / credit
# real assets
# volatility
# fixed income yield
# foreign exchange
# commodities
# consumer price index
