import pandas as pd
import seaborn as sns
import os
import yfinance as yf
import matplotlib.pyplot as plt
import dataframe_image as dfi
from pdfConverter import save_multi_image
from matplotlib import rc

rc('mathtext', default='regular')
plt.rcParams["figure.autolayout"] = True
pd.set_option('display.max_columns', None)

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
    a = yf.Ticker(str(index)).history(period="3Y") # how many years of data
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

# adding a percent change column to our data


# checkin our df
print(appendedData)

# exporting out data as a csv file
appendedData.to_csv('equityIndicesHistData.csv', index=False)

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

fig0 = plt.figure()
all = sns.lineplot(data=appendedData, x='Date', y='Close',
                   hue='Ticker', linewidth=0.7, ci=None,
                   legend=True).set(title='All Indices - Close')
fig1 = plt.figure()
delta = sns.lineplot(data=appendedData, x='Date', y='Delta',
                     hue='Ticker', linewidth=0.6, ci=None,
                     legend=True).set(title='% Change All Indices')

# some stylistic changes
for ax in fig.axes:
    ax.tick_params(labelrotation=90, axis='x')
    ax.set(xlabel=None)

filename = 'equityIndices.pdf'
save_multi_image(filename)

