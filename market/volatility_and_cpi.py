# purpose is to gather data related to volatility and print our a plot
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os
import datetime
from blackBox.bls_data_processor import fetch_bls_series
import seaborn as sns
from datetime import datetime
import datetime
from matplotlib import rc

rc('mathtext', default='regular')

plt.rcParams["figure.autolayout"] = True

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# finding ticker symbol for volatility on yfinance
volatility_index = yf.Ticker("^VIX")
# converting information on vix --> dictionary
vix_dict = volatility_index.info
# getting historical market data
hist_data = volatility_index.history(period='1Y')

# now we will be filtering out to only data that we need into a df
filtered_vix = {key: vix_dict[key] for key in vix_dict.keys() & {
    'shortName', 'symbol', 'previousClose', 'regularMarketOpen',
    'twoHundredDayAverage', 'regularMarketPreviousClose', 'fiftyDayAverage',
    'open', 'fiftyTwoWeekHigh', 'fiftyTwoWeekLow', 'regularMarketPrice'
}}

# converting our filtered dictionary into a df
vix_df = pd.DataFrame(filtered_vix, index = [0, ])
vix_df = vix_df.sort_index(axis=1)

# adding col of percent change of index
vix_df = vix_df.assign(percentChange = (vix_df['regularMarketOpen'] - vix_df[
    'regularMarketPreviousClose']) / vix_df['regularMarketPreviousClose']*100)

# plotting the percent change
# vix_df.plot(x='shortName', y='percentChange', kind='bar')

# adding a percent change col to historical data df
hist_data = hist_data.assign(percentChange = hist_data['Open'].pct_change())

# please note that historical data is already a df so we can plot it
'''
ax1 = plt.subplot()
l1, = ax1.plot(hist_data['Open'], color='blue')
ax1.set_ylabel('VIX Index Value')
ax2 = ax1.twinx()
ax2.set_ylabel('% Change VIX')
l2, = ax2.plot(hist_data['percentChange'], color='pink', alpha=0.5)
plt.legend([l1, l2], ['VIX Value', '% Change'])
plt.title("CBOE Volatility Index")
# plt.show()
'''

# ______________________________________________________________________________
# BLS API DATA FROM HERE AND DOWN
# grabbing data from bls public api
# we want to grab the bls from our virtual environment
bls_api_key = os.environ.get('blsAPI')

# series id of interest
unemployment_rate = "LNS14000000"
cpi = "CUUR0000SA0" # consumer price index
eci = "CIU1010000000000A" # employment cost index
imports = "EIUIR" # imports all commodities
exports = "EIUIQ" # exports, all commodities

# setting up our series list
series = [unemployment_rate, cpi, eci, imports, exports]
end_year = datetime.datetime.now().year
start_year = end_year - 5

# grabbing bls api data
bls_data = fetch_bls_series(series, startyear=start_year, endyear=end_year,
                            registrationKey=bls_api_key)


'''
Looking at our bls data structure we see the following:
*level 1: 
- {4 props}
**Level 2: 
- status:
- responseTime
- message
- Results
***Level 3 [Results unnest]:
- series
    - 0
        - seriesID:
        - data:
            - 0:
                - year
                - period
                -periodName
                -latest
                - value
            - 1:
            - ...
            - M
    - 1
    - ...
    - N
    
So it seems that we only care about first grabbing props in series which 
each index contains specific information requested. for instance, if we req
5 series id, then N = 5. best way to move forward would be to allocate a df 
for each series index, grab seriesID and add it to a df that grabbed data per
series index. once we have N df's, then given they are similar in structure, we
just need to vertically concatenate them and there we have 1 master df.
'''

# purpose is to only grab the results -> series list which containts 2 things
# first, the seriesID and second, the data!
blsDataList = bls_data['Results']['series']

# creating an empty df to add incoming dfs
blsMainDF = pd.DataFrame(columns=['seriesID'])

# purpose is now to loop through each item and add to a general pandas df
for item in blsDataList:
    blsMainDF = pd.concat([blsMainDF, pd.DataFrame(data=item['data'])])
    if blsMainDF['seriesID'].isnull:
        blsMainDF['seriesID'].fillna(item['seriesID'], inplace=True)
    else:
        continue


# removing columns we do not need such as footnotes and latest cols
blsMainDF = blsMainDF.drop(['latest', 'footnotes'], axis=1)

# converting year and period to string to manipulate it
# blsMainDF[['year', 'period']] = blsMainDF[['year', 'period']].astype(str)

# dropping M from period column

# now we are adding date column
blsMainDF['Date'] = blsMainDF['periodName'] + "-" + blsMainDF['year']

# excludes eci which only collects every quarter on data
blsNonECI = blsMainDF[blsMainDF['seriesID'] != 'CIU1010000000000A']

blsNonECI['Date'] = pd.to_datetime(blsNonECI['Date'])
blsNonECI = blsNonECI.reset_index(drop=True)

'''
now we want to create graphs for the 5 given data types
'''
sns.set(font_scale=0.7)
fig, axes = plt.subplots(2, 2)
fig.suptitle('U.S. Bureau of Labor Statistics Insights')

fig1 = sns.scatterplot(ax=axes[0, 0], data=blsNonECI[blsNonECI['seriesID'] ==
                                                  'LNS14000000'], x='Date',
                    y='value', linewidth=0.7, ci=None).set(title='Unemployment')

fig2 = sns.lineplot(ax=axes[0, 1], data=blsNonECI[blsNonECI['seriesID'] ==
                                                  'CUUR0000SA0'], x='Date',
                    y='value', linewidth=0.7, ci=None).set(title='CPI')

fig3 = sns.lineplot(ax=axes[1, 0], data=blsNonECI[blsNonECI['seriesID'] ==
                                                  'EIUIR'], x='Date',
                    y='value', linewidth=0.7, ci=None).set(title='Imports, '
                                                                 'All '
                                                                 'Commodities')

fig4 = sns.lineplot(ax=axes[1, 1], data=blsNonECI[blsNonECI['seriesID'] ==
                                                  'EIUIQ'], x='Date',
                    y='value', linewidth=0.7, ci=None).set(title='Exports, '
                                                                 'All '
                                                                 'Commodities')

for ax in fig.axes:
    ax.tick_params(labelrotation=90, axis='x')

print(blsNonECI)
plt.show()
