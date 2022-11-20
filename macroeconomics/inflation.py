from black_box.pdfConverter import save_multi_image
'''
Purpose of the script is to present some key data_visuals as it relates to inflation
1. Inflation over time, USD
    a. data: [1] CPI, CPI (seasonally adjusted), PPI, GDP Deflator
    b. data: [2] SD in CPI
    c. x axis: YTD, 3 years, 5 years, and 10 years
2. Inflation Expectations
    a. data: [1] UMichigan Survey, consumer expecations of inflation
    b. data: [2] NY fed survey of consumer expectation
3. TreasuryMarket Expected Inflation
    a. data: [1] implied expected inflation, T. Bond Rate, TIPs rate
    b. dataSetup: [1] delta(tbond, tips) == measure of financial_markets expexted inflation
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
from black_box.bls_data_processor import fetch_bls_series
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from datetime import date

# time related stuff
today = date.today()
currentDate = today.strftime('%m_%d_%y')

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
fredDf.reset_index(inplace=True)
fredDf = fredDf.rename(columns = {'index':'Date'})

# grabbing cpi and cpi seasonally adjusted data from bls
series = [cpi, cpi_adj]
end_year = datetime.datetime.now().year
start_year = end_year - 15

# officially grabbing our data with our params
blsMainDF = fetch_bls_series(series, startyear=start_year, endyear=end_year,
                            registrationKey=blsKey)

fredDf.to_csv('.\data_files\economic_fred_data.csv', index=False)
blsMainDF.to_csv('.\data_files\economic_bls_data.csv', index=False)


fig1 = plt.figure()
line1 = sns.lineplot(data=fredDf, x='Date', y='GDP Def')
line2 = sns.lineplot(data=blsMainDF, x='Date', y='value', hue='seriesID')


filename = '.\data_visuals\inflation_visuals_'

save_multi_image(filename + currentDate + '.pdf')
