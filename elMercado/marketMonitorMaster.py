import pandas as pd
import seaborn as sns
import os
import yfinance as yf
import matplotlib.pyplot as plt
import dataframe_image as dfi
from pdfConverter import save_multi_image
from matplotlib import rc
from datetime import date

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
- s&p 500 index
- nasdaq composite index
- russell 1000 index
- russell 1000 value index
- russell 1000 growth index
- russell 2000 index
- russell 2000 value index
- russell 2000 growth index
'''
# creating a list of equity indices
equityIndices = ['^IXIC', '^RUI', '^RLV', '^RLG', '^RUT', '^RUJ',
                 '^RUO', '^NDX', '^DJI']

# create a empty dataframe
appendedData = pd.DataFrame(columns=['Ticker'])

# what we want to grab from info
topics = {'shortName'}

# process to grab historical data
for index in equityIndices:
    a = yf.Ticker(str(index)).history(period="5Y") # how many years of data
    a.drop(['Dividends', 'Stock Splits', 'Volume'], inplace=True, axis=1)
    a = a.assign(Delta=a['Close'].pct_change())
    # info = yf.Ticker(str(index)).info
    #filterInfo = {key: info[key] for key in info.keys() & topics}
    #filterInfo = pd.DataFrame(filterInfo, index=[0, ])
    appendedData = pd.concat([appendedData, pd.DataFrame(a)])
    #appendedData = pd.concat([appendedData, filterInfo])
    if appendedData['Ticker'].isnull:
        appendedData['Ticker'].fillna(index, inplace=True)
    else:
        continue


# resetting our index
appendedData.reset_index(inplace=True)

# renaming the column holding date values
appendedData.rename(columns={'index':'Date'}, inplace=True)

# converting our date column to a date value
appendedData['Date'] = pd.to_datetime(appendedData['Date'])

# checkin our df
print(appendedData)

# exporting out data as a csv file
appendedData.to_csv('.\data_csv_format\equityIndicesHistData.csv', index=False)

'''
at this point we want to create a number of figures that provides us with 
insights on the historical data we have now collected 
'''

# creating subsets of data to present in a figure format
ixicOnly = appendedData[appendedData['Ticker'] == '^IXIC']
ruiOnly = appendedData[appendedData['Ticker'] == '^RUI']
rlvOnly = appendedData[appendedData['Ticker'] == '^RLV']
rlgOnly = appendedData[appendedData['Ticker'] == '^RLG']
rutOnly = appendedData[appendedData['Ticker'] == '^RUT']
rujOnly = appendedData[appendedData['Ticker'] == '^RUJ']
ruoOnly = appendedData[appendedData['Ticker'] == '^RUO']
ndxOnly = appendedData[appendedData['Ticker'] == '^NDX']
djiOnly = appendedData[appendedData['Ticker'] == '^DJI']


# setting up our graph information
sns.set(font_scale=0.5)
fig, axes = plt.subplots(3, 3)
fig.suptitle('Equity Indices Historical Information')

# purpose is to create a number of figures reflecting data
# this will cover one figure and will be faceted
dji = sns.lineplot(ax=axes[0, 0], data=djiOnly, x='Date', y='Close',
                   linewidth=0.7,
                   ci=None).set(title='Dow Jones Industrial Average (^DJI)')

ixic = sns.lineplot(ax=axes[0,1], data=ixicOnly, x='Date', y='Close',
                    linewidth=0.7,
                    ci=None).set(title='NASDAQ Composite (^IXIC)')

rui = sns.lineplot(ax=axes[0,2], data=ruiOnly, x='Date', y='Close',
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

# purpose is to plot all indices close in figure 2 of the pdf
fig0 = plt.figure()
all = sns.lineplot(data=appendedData, x='Date', y='Close',
                   hue='Ticker', linewidth=0.7, ci=None,
                   legend=True).set(title='All Indices - Close')

# plan is to plot all % change of all indices in one figure aka figure 3
fig1 = plt.figure()
delta = sns.lineplot(data=appendedData, x='Date', y='Delta',
                     hue='Ticker', linewidth=0.6, ci=None,
                     legend=True).set(title='% Change All Indices')

# setting up our graph information
sns.set(font_scale=0.5)
fig, axes = plt.subplots(3, 3)
fig.suptitle('Equity Indices Historical % Change')

# purpose is to create a facet grid of % change of all indices
dji_delta = sns.lineplot(ax=axes[0, 0], data=djiOnly, x='Date', y='Delta',
                   linewidth=0.5,
                   ci=None).set(title='Dow Jones Industrial Average (^DJI)')

ixic_delta = sns.lineplot(ax=axes[0,1], data=ixicOnly, x='Date', y='Delta',
                    linewidth=0.5,
                    ci=None).set(title='NASDAQ Composite (^IXIC)')

rui_delta = sns.lineplot(ax=axes[0,2], data=ruiOnly, x='Date', y='Delta',
                   linewidth=0.5, ci=None).set(title='Russell 1000 (^RUI)')

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

'''
Okay now that we are able to grab and transform data from equity indices, let's
do it for fixed income yield aka the following:
- US fed rate
- us 3 month
- us 1 year
- us 2 year
- us 5 year
- us 10 year
- us 30 year
further we will want to create a visual of this newly plotted yield curve where
the hue change in color is tracked by year
'''
# purpose is to create ticker symbol for fixed income indices
fi_indices = ['^IRX', '^FVX', '^TNX', '^TYX']

# where we will be adding gathered data
fi_appendedData = pd.DataFrame(columns=['Ticker'])

# process to grab historical data
for index in fi_indices:
    a = yf.Ticker(str(index)).history(period="5Y") # how many years of data
    a.drop(['Dividends', 'Stock Splits', 'Volume'], inplace=True, axis=1)
    a = a.assign(Delta=a['Close'].pct_change())
    # info = yf.Ticker(str(index)).info
    #filterInfo = {key: info[key] for key in info.keys() & topics}
    #filterInfo = pd.DataFrame(filterInfo, index=[0, ])
    fi_appendedData = pd.concat([fi_appendedData, pd.DataFrame(a)])
    #appendedData = pd.concat([appendedData, filterInfo])
    if fi_appendedData['Ticker'].isnull:
        fi_appendedData['Ticker'].fillna(index, inplace=True)
    else:
        continue

# resetting our index
fi_appendedData.reset_index(inplace=True)

# renaming the column holding date values
fi_appendedData.rename(columns={'index':'Date'}, inplace=True)

# converting our date column to a date value
fi_appendedData['Date'] = pd.to_datetime(appendedData['Date'])


# purpose is to plot all fi indices
fig2 = plt.figure()
allFi = sns.lineplot(data=fi_appendedData, x='Date', y='Close',
                   hue='Ticker', linewidth=0.7, ci=None,
                   legend=True).set(title='All FI Indices - Close')

# exporting out data as a csv file
appendedData.to_csv('.\data_csv_format\FIIndicesHistData.csv', index=False)

# some stylistic changes
for ax in fig.axes:
    ax.tick_params(labelrotation=90, axis='x')
    ax.set(xlabel=None)

filename = 'equityIndices_'
save_multi_image(filename + currentDate + '.pdf')

