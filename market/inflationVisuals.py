'''
Purpose of the script is to present some key visuals as it relates to inflation
1. Inflation over time, USD
    a. data: [1] CPI, CPI (seasonally adjusted), PPI, GDP Deflator
    b. data: [2] SD in CPI
    c. x axis: YTD, 3 years, 5 years, and 10 years
2. Inflation Expectations
    a. data: [1] UMichigan Survey, consumer expecations of inflation
    b. data: [2] NY fed survey of consumer expectation
3. TreasuryMarket Expected Inflation
    a. data: [1] implied expected inflation, T. Bond Rate, TIPs rate
    b. dataSetup: [1] delta(tbond, tips) == measure of market expexted inflation
    c. x axis: 1 year
4. Expected inflation term sttructure
    a. extension of [3]
    b. topics(lines on graph): current month, prevous month, YTD
    c. YTD data: 3 curves for the year, aka delta(TBond, TIPs) from 1Y to 30Y
'''
import os
import fredapi as fa
import pandas as pd
import datetime
from blackBox.bls_data_processor import fetch_bls_series

# setting up any api keys that we may need
fredKey = os.environ.get('FREDKEY')
blsKey = os.environ.get('BLSKEY')

# figure 1
cpi = "CUUR0000SA0"  # series id from bls
cpi_adj = "CUSR0000SA0" # searies id from bls, seasonally adjusted
ppi = 0

# grabbing gdp deflator data
fred = fa.Fred(api_key=fredKey)
gdp_deflator = fred.get_series("GDPDEF")  # percent change from a year ago
gdp_deflator.name = 'GDP Def'

# converting data from fred into df
fredDf = pd.DataFrame(data=gdp_deflator)

# grabbing cpi and cpi seasonally adjusted data from bls
series = [cpi, cpi_adj]
end_year = datetime.datetime.now().year
start_year = end_year - 5

# officially grabbing our data with our params
bls_data = fetch_bls_series(series, startyear=start_year, endyear=end_year,
                            registrationKey=blsKey)
# purpose is to grab the results -> series list which contains 2 things
# first, the series ID and second, the data!
blsDataList = bls_data['Results']['series']

# creating an empty df to add incoming dfs
blsMainDF = pd.DataFrame(columns=['seriesID'])

# purpose is to loop through each item and add to a general pandas df
for item in blsDataList:
    blsMainDF = pd.concat([blsMainDF, pd.DataFrame(data=item['data'])])
    if blsMainDF['seriesID'].isnull:
        blsMainDF['seriesID'].fillna(item['seriesID'], inplace=True)
    else:
        continue

# removing columns we do not need such as footnotes and latest cols
blsMainDF = blsMainDF.drop(['latest', 'footnotes'], axis=1)

# purpose is to add a date column
blsMainDF['Date'] = blsMainDF['periodName'] + '-' + blsMainDF['year']
blsMainDF['Date'] = pd.to_datetime(blsMainDF['Date'])
blsMainDF = blsMainDF.reset_index(drop=True)
blsMainDF['value'] = blsMainDF['value'].astype(float)

print(blsMainDF)

