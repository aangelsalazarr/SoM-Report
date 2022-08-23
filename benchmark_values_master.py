# purpose of this file is to provide benchmark values on financial markets
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

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
appended_data = []

for index in equity_indices:
    a = yf.Ticker(str(index)).info
    filtered_a = {key: a[key] for key in a.keys() & {
        'shortName', 'regularMarketOpen',
        'twoHundredDayAverage', 'fiftyTwoWeekHigh',
        'regularMarketPreviousClose', 'ytdReturn',
    }}
    df = pd.DataFrame(filtered_a, index=[str(index_value), ])
    df = df.sort_index(axis=1)
    index_value += 1
    appended_data.append(df)

# combining all of our dfs into 1 df
appended_data = pd.concat(appended_data)

# viewing our new df; good to go!
# print(appended_data)

# add a new col that tracks percentage change of price
appended_data = appended_data.assign(percentChange=(appended_data[
                                                        "regularMarketOpen"] -
                                                    appended_data[
                                                        "regularMarketPreviousClose"]) /
                                                   appended_data[
                                                       "regularMarketPreviousClose"] * 100)

# conditional color statement
# colors = ["red" if float(appended_data["percentChange"]) < 0 else "green"]

# now let's plot our data
appended_data.plot(x='shortName', y='percentChange', kind='bar')
plt.title("Index Price % Change (Market Open vs Market Previous Close)")
plt.xlabel("Index")
plt.ylabel("Percent Change (%)")
plt.axhline(y=0, color="green")
# plt.show()

# fixed income / credit
# real assets
# volatility
# fixed income yield
# foreign exchange
# consumer price index
# commodities
commodities_indices = []

# crypto related reference entities
crypto_indices = ["BTC-USD", "ETH-USD", "USDT-USD", "USDC-USD", "BNB-USD"]
index_val = 0
appended_cryptos = []

# here we are automating the creation of a master df
for crypto in crypto_indices:
    cryp = yf.Ticker(str(crypto)).info
    filtered_cryp = {key: cryp[key] for key in cryp.keys() & {
        'fiftyTwoWeekHigh', 'ytdReturn',
        'priceToSalesTrailing12Months',
        'marketCap', 'beta',
        'regularMarketPreviousClose',
        'averageDailyVolume10Day', 'volume24Hr', 'payoutRatio',
        'regularMarketOpen', 'name',
    }}

    df = pd.DataFrame(filtered_cryp, index=[str(index_val), ])
    df = df.sort_index(axis=1)
    index_val += 1
    appended_cryptos.append(df)

# now we want to combine all of the dfs into one master df
appended_cryptos = pd.concat(appended_cryptos)

# checking to see if it worked
print(appended_cryptos)
