import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt
from pdfConverter import save_multi_image
from matplotlib import rc
from datetime import date
from dateutil.relativedelta import relativedelta
from yfinance_data_processor import data_processor
from eia_data_processor import grab_eia_data

# some params related to the framework of output that we will need
rc('mathtext', default='regular')
plt.rcParams["figure.autolayout"] = True
pd.set_option('display.max_columns', None)

# purpose is to create current date and current year function
today = date.today()
currentDate = today.strftime('%m%d%y')

'''
The purpose of this file is to grab all relevant data on equity indices. The 
following will be tracked along with date data type:
    s&p 500 index, nasdaq composite index, russell 1000 index, russell 1000 
    value index, russell 1000 growth index, russell 2000 index, russell 2000 
    value index, russell 2000 growth index
'''
# creating a list of equity indices
equityIndices = ['^IXIC', '^RUI', '^RLV', '^RLG', '^RUT', '^RUJ',
                 '^RUO', '^NDX', '^DJI']

# create a empty dataframe
ei_df = pd.DataFrame(columns=['Ticker'])

# what we want to grab from info
topics = {'shortName'}

# process to grab historical data
ei_df = data_processor(list=equityIndices, period='ytd')

# exporting out data as a csv file
ei_df.to_csv('.\data_csv_format\equityIndicesHistData.csv', index=False)

'''
at this point we want to create a number of figures that provides us with 
insights on the historical data we have now collected 
'''

# creating subsets of data to present in a figure format
ixicOnly = ei_df[ei_df['Ticker'] == equityIndices[0]]
ruiOnly = ei_df[ei_df['Ticker'] == equityIndices[1]]
rlvOnly = ei_df[ei_df['Ticker'] == equityIndices[2]]
rlgOnly = ei_df[ei_df['Ticker'] == equityIndices[3]]
rutOnly = ei_df[ei_df['Ticker'] == equityIndices[4]]
rujOnly = ei_df[ei_df['Ticker'] == equityIndices[5]]
ruoOnly = ei_df[ei_df['Ticker'] == equityIndices[6]]
ndxOnly = ei_df[ei_df['Ticker'] == equityIndices[7]]
djiOnly = ei_df[ei_df['Ticker'] == equityIndices[8]]

# setting up our graph information
sns.set(font_scale=0.5)
fig, axes = plt.subplots(3, 3)
fig.suptitle('Equity Indices Historical Information')

# purpose is to create a number of figures reflecting data
# this will cover one figure and will be faceted
dji = sns.lineplot(ax=axes[0, 0], data=djiOnly, x='Date', y='Close',
                   linewidth=0.7,
                   ci=None).set(title='Dow Jones Industrial Average (^DJI)')

ixic = sns.lineplot(ax=axes[0, 1], data=ixicOnly, x='Date', y='Close',
                    linewidth=0.7,
                    ci=None).set(title='NASDAQ Composite (^IXIC)')

rui = sns.lineplot(ax=axes[0, 2], data=ruiOnly, x='Date', y='Close',
                   linewidth=0.7, ci=None).set(title='Russell 1000 (^RUI)')

rlv = sns.lineplot(ax=axes[1, 0], data=rlvOnly, x='Date', y='Close',
                   linewidth=0.7,
                   ci=None).set(title='Russell 1000 Value (^RLV)')

rlg = sns.lineplot(ax=axes[2, 0], data=rlgOnly, x='Date', y='Close',
                   linewidth=0.7,
                   ci=None).set(title='Russell 1000 Growth (^RLG)')

rut = sns.lineplot(ax=axes[1, 2], data=rutOnly, x='Date', y='Close',
                   linewidth=0.7,
                   ci=None).set(title='Russell 2000 (^RUT)')

ruj = sns.lineplot(ax=axes[1, 1], data=rujOnly, x='Date', y='Close',
                   linewidth=0.7,
                   ci=None).set(title='Russell 2000 Value (^RUJ)')

ruo = sns.lineplot(ax=axes[2, 1], data=ruoOnly, x='Date', y='Close',
                   linewidth=0.7,
                   ci=None).set(title='Russell 2000 Growth (^RUO)')

ndx = sns.lineplot(ax=axes[2, 2], data=ndxOnly, x='Date', y='Close',
                   linewidth=0.7,
                   ci=None).set(title='NASDAQ 100 (^NDX)')

# purpose is to plot all indices close in figure 2 of the pdf above 5k in value
fig0a = plt.figure()
all = sns.lineplot(data=ei_df[ei_df['Close'] > 5000],
                   x='Date', y='Close',
                   hue='Ticker', linewidth=0.7, ci=None,
                   legend=True).set(title='All Indices - Close')

# purpose is to plot all indices close in figure 2 of the pdf above 5k in value
fig0b = plt.figure()
allb = sns.lineplot(data=ei_df[ei_df['Close'] < 5000],
                   x='Date', y='Close',
                   hue='Ticker', linewidth=0.7, ci=None,
                   legend=True).set(title='All Indices - Close')

# plan is to plot all % change of all indices in one figure aka figure 3 above
fig1 = plt.figure()
delta = sns.lineplot(data=ei_df, x='Date', y='Delta',
                     hue='Ticker', linewidth=0.6, ci=None,
                     legend=True).set(title='% Change All Indices')

# setting up our graph information
sns.set(font_scale=0.5)
fig, axes = plt.subplots(3, 3)
fig.suptitle('Equity Indices Historical % Change')

# purpose is to create a facet grid of % change of all indices
dji_delta = sns.lineplot(ax=axes[0, 0], data=djiOnly, x='Date', y='Delta',
                         linewidth=0.5,
                         ci=None).set(
    title='Dow Jones Industrial Average (^DJI)')

ixic_delta = sns.lineplot(ax=axes[0, 1], data=ixicOnly, x='Date', y='Delta',
                          linewidth=0.5,
                          ci=None).set(title='NASDAQ Composite (^IXIC)')

rui_delta = sns.lineplot(ax=axes[0, 2], data=ruiOnly, x='Date', y='Delta',
                         linewidth=0.5, ci=None).set(
    title='Russell 1000 (^RUI)')

rlv_delta = sns.lineplot(ax=axes[1, 0], data=rlvOnly, x='Date', y='Delta',
                         linewidth=0.5,
                         ci=None).set(title='Russell 1000 Value (^RLV)')

rlg_delta = sns.lineplot(ax=axes[2, 0], data=rlgOnly, x='Date', y='Delta',
                         linewidth=0.5,
                         ci=None).set(title='Russell 1000 Growth (^RLG)')

rut_delta = sns.lineplot(ax=axes[1, 2], data=rutOnly, x='Date', y='Delta',
                         linewidth=0.5,
                         ci=None).set(title='Russell 2000 (^RUT)')

ruj_delta = sns.lineplot(ax=axes[1, 1], data=rujOnly, x='Date', y='Delta',
                         linewidth=0.5,
                         ci=None).set(title='Russell 2000 Value (^RUJ)')

ruo_delta = sns.lineplot(ax=axes[2, 1], data=ruoOnly, x='Date', y='Delta',
                         linewidth=0.5,
                         ci=None).set(title='Russell 2000 Growth (^RUO)')

ndx_delta = sns.lineplot(ax=axes[2, 2], data=ndxOnly, x='Date', y='Delta',
                         linewidth=0.5,
                         ci=None).set(title='NASDAQ 100 (^NDX)')

################################################################################
################################################################################
################################################################################

'''
Okay now that we are able to grab and transform data from equity indices, let's
do it for fixed income yield aka the following:
    US fed rate, us 3 month, us 1 year, us 2 year, us 5 year, us 10 year, 
    us 30 year
'''
# purpose is to create ticker symbol for fixed income indices
fi_indices = ['^IRX', '^FVX', '^TNX', '^TYX']

# where we will be adding gathered data
fi_df = pd.DataFrame(columns=['Ticker'])

# process to grab historical data
fi_df = data_processor(list=fi_indices, period='ytd')

# purpose is to plot all fi indices
fig2 = plt.figure()
allFi = sns.lineplot(data=fi_df, x='Date', y='Close',
                     hue='Ticker', linewidth=0.7, ci=None,
                     legend=True).set(title='All FI Indices - Close')

# exporting out data as a csv file
fi_df.to_csv('.\data_csv_format\FIIndicesHistData.csv', index=False)

################################################################################
################################################################################
'''
Now, we will be gathering data for foreign exchange rates
    EUR-USD Spot Rate, USD-JPY spot rate, GBP-USD spot rate, CHF-USD spot rate (
    USD-CHF spot rate inverted), AUD-USD spot rate, CAD-USD spot rate (USD-CAD 
    spot rate inverted)
'''
# creating a list of tickery symbols for the ticker we want specifically
fxIndices = ['EURUSD=X', 'JPY=X', 'GBPUSD=X', 'AUDUSD=X', 'MXN=X',
             'CHFUSD=X', 'CADUSD=X', 'NZDUSD=X', 'RUB=X']

# where we will be adding gathered data
fx_df = pd.DataFrame(columns=['Ticker'])

# process to grab historical data
fx_df = data_processor(list=fxIndices, period='ytd')

# exporting out data as a csv file
fx_df.to_csv('.\data_csv_format\FXIndicesHistData.csv', index=False)

# partitioning our dfs
eurUSDOnly = fx_df[fx_df['Ticker'] == 'EURUSD=X']
jpyUSDOnly = fx_df[fx_df['Ticker'] == 'JPY=X']
gbpUSDOnly = fx_df[fx_df['Ticker'] == 'GBPUSD=X']
audUSDOnly = fx_df[fx_df['Ticker'] == 'AUDUSD=X']
mxnUSDOnly = fx_df[fx_df['Ticker'] == 'MXN=X']
chfUSDOnly = fx_df[fx_df['Ticker'] == 'CHFUSD=X']
cadUSDOnly = fx_df[fx_df['Ticker'] == 'CADUSD=X']
nzdUSDOnly = fx_df[fx_df['Ticker'] == 'NZDUSD=X']
rubUSDOnly = fx_df[fx_df['Ticker'] == 'RUB=X']

# setting up our graph information
sns.set(font_scale=0.5)
fig, axes = plt.subplots(3, 3)
fig.suptitle('FX Indices Historical Data, Close')

# purpose is to create a facet grid of % change of all indices
eur_usd = sns.lineplot(ax=axes[0, 0], data=eurUSDOnly, x='Date', y='Close',
                       linewidth=0.5,
                       ci=None).set(title='EUR-USD Spot Rate, Close')

jpy_usd = sns.lineplot(ax=axes[0, 1], data=jpyUSDOnly, x='Date', y='Close',
                       linewidth=0.5,
                       ci=None).set(title='JPY-USD Spot Rate, Close')

gbp_usd = sns.lineplot(ax=axes[0, 2], data=gbpUSDOnly, x='Date', y='Close',
                       linewidth=0.5, ci=None).set(
    title='GBP-USD Spot Rate, Close')

aud_usd = sns.lineplot(ax=axes[1, 0], data=audUSDOnly, x='Date', y='Close',
                       linewidth=0.5,
                       ci=None).set(title='AUD-USD Spot Rate, Close')

mxn_usd = sns.lineplot(ax=axes[2, 0], data=mxnUSDOnly, x='Date', y='Close',
                       linewidth=0.5,
                       ci=None).set(title='MXN-USD Spot Rate, Close')

chf_usd = sns.lineplot(ax=axes[1, 2], data=chfUSDOnly, x='Date', y='Close',
                       linewidth=0.5,
                       ci=None).set(title='CHF-USD Spot Rate, Close')

cad_usd = sns.lineplot(ax=axes[1, 1], data=cadUSDOnly, x='Date', y='Close',
                       linewidth=0.5,
                       ci=None).set(title='CAD-USD Spot Rate, Close')

nzd_usd = sns.lineplot(ax=axes[2, 1], data=nzdUSDOnly, x='Date', y='Close',
                       linewidth=0.5,
                       ci=None).set(title='NZD-USD Spot Rate, Close')

rub_usd = sns.lineplot(ax=axes[2, 2], data=rubUSDOnly, x='Date', y='Close',
                       linewidth=0.5,
                       ci=None).set(title='RUB-USD Spot Rate, Close')

################################################################################
################################################################################
'''
Now, we will be gathering data for commodities in the following order
- wti 1 month forward contract
- natural gas 1 month forward contract
- gold 2 month forward contract
- copper 2 month forward contract
- aluminum 2 month forward contract 
- platinum 2 month forward contract
- palladium months forward contract
- silver forward contract
'''
# creating a list of ticker symbols for commodity futures
# need to find wti futures historical data because it is not presented on
# yfinance
commodityIndices = ['NG=F', 'GC=F', 'HG=F', 'ALI=F', 'PL=F', 'PA=F',
                    'SI=F']

# where we will be adding gathered data
commodities_df = pd.DataFrame(columns=['Ticker'])

# process to grab historical data
commodities_df = data_processor(list=commodityIndices, period='ytd')

# purpose is to plot all commodity indices with values greater than 500
fig4 = plt.figure()
allComa = sns.lineplot(data=commodities_df[commodities_df['Close'] > 500],
                       x='Date', y='Close',
                       hue='Ticker', linewidth=0.7, ci=None,
                       legend=True).set(title='All Commodity Indices - Close')

# purpose is to plot all commodity indices with values less than 500
fig5 = plt.figure()
allComb = sns.lineplot(data=commodities_df[commodities_df['Close'] < 500],
                       x='Date', y='Close',
                       hue='Ticker', linewidth=0.7, ci=None,
                       legend=True).set(title='All Commodity Indices - Close')

# exporting out data as a csv file
commodities_df.to_csv('.\data_csv_format\ComIndicesHistData.csv', index=False)

# the purpose of this section is to grab petroleum data from the EIA open data
# first we want to retrieve our api key and make sure it is good to go
apiKey = os.environ.get('eiaAPI')

# api endpoint; will be adding specifics at the end of URL
URL = "https://api.eia.gov/v2/"

# here are the specifics of what we are looking for
specificReq = "petroleum/pri/spt/data/"

# petroleum pricing API endpoint
petroPricesURL = URL + specificReq + "?api_key=" + str(apiKey)

'''
X-Params: {
    "frequency": "daily",
    "data": [
        "value"
    ],
    "facets": {},
    "start": null,
    "end": null,
    "sort": [
        {
            "column": "period",
            "direction": "desc"
        }
    ],
    "offset": 0,
    "length": 5000,
    "api-version": "2.0.2"
}
'''
# purpose is to create a date specific to eia req
startDate = today - relativedelta(years=5)
startDateEIA = startDate.strftime("%Y-%m-%d")

# now we will be translating our params into the url request
dataInput = "&data[0]=value"
facetsInput = ""
frequencyInput = "&frequency=weekly"
startDateInput = "&start=" + str(startDateEIA)

# adding everything up
petroPricesURL = petroPricesURL + dataInput + frequencyInput + startDateInput
print(petroPricesURL)

# sending get request and saving the response as a response object
eia_df = grab_eia_data(url=petroPricesURL)

# creating specific data with and without wti data
value_list = ["EPCWTI", "EPCBRENT"]
petro_df_wti = eia_df[eia_df['product'].isin(value_list)]
petro_df_non_wti = eia_df[~eia_df['product'].isin(value_list)]

# purpose is to plot all petro spot prices but split between wti and non wti
fig6 = plt.figure()
petro_exclude_wti = sns.lineplot(data=petro_df_non_wti,
                       x='period', y='value',
                       hue='product-name', linewidth=0.7, ci=None,
                       legend=True).set(title='Petroleum Spot Prices, Weekly')

fig7 = plt.figure()
petro_wti = sns.lineplot(data=petro_df_wti, x='period', y='value',
                         hue='product-name', linewidth=0.7, ci=None,
                         legend=True).set(title='WTI Spot Prices, Weekly')


# exporting out data as a csv file
petro_df.to_csv('.\data_csv_format\petro_spot_prices_eia.csv', index=False)

################################################################################
################################################################################

# some stylistic changes
for ax in fig.axes:
    ax.tick_params(labelrotation=90, axis='x')
    ax.set(xlabel=None)

filename = '.\market_monitor_visuals\marketMonitor_'
save_multi_image(filename + currentDate + '.pdf')


