# purpose is to gather data related to fixed income
import yfinance as yf
from fredapi import Fred
import os
import pandas as pd


# 3 months, 5 year, 10 year, 30 year respectively
fixed_income_indices = ['^IRX', '^FVX', '^TNX', '^TYX']

index_value = 0
appended_data = []

for index in fixed_income_indices:
    a = yf.Ticker(str(index)).info
    filtered_a = {key: a[key] for key in a.keys() & {
        'shortName', 'regularMarketOpen',
        'twoHundredDayAverage', 'fiftyDayAverage',
        'regularMarketPreviousClose',
    }}
    df = pd.DataFrame(filtered_a, index=[str(index_value), ])
    df = df.sort_index(axis=1)
    index_value += 1
    appended_data.append(df)

# combining all of our dfs into 1 df
appended_data = pd.concat(appended_data)

print(appended_data)

# federal funds rate data
fred_api_key = os.environ['fredapi']
fred = Fred(api_key=fred_api_key)
fedFundsRate = fred.get_series_latest_release('FEDFUNDS')
gdp = fred.get_series_all_releases('GDP')
print(fedFundsRate)
print(gdp)
