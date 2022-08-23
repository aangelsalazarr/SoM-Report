# purpose is to gather data related to fixed income
import yfinance as yf
from fredapi import Fred
import os


# 3 months, 5 year, 10 year, 30 year respectively
fixed_income_indices = ['^IRX', '^FVX', '^TNX', '^TYX']

# federal funds rate data
fred_api_key = os.environ['fredapi']
fred = Fred(api_key=fred_api_key)
fedFundsRate = fred.get_series_latest_release('FEDFUNDS')
gdp = fred.get_series_all_releases('GDP')
print(fedFundsRate)
print(gdp)
