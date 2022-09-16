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
                 '^RUO']

# create a empty dataframe
appendedData = pd.DataFrame(columns=['Ticker'])

# process to grab historical data
for index in equityIndices:
    a = yf.Ticker(str(index)).history(period="3Y") # how many years of data
    # a.reset_index(inplace=True)
    a.drop(['Dividends', 'Stock Splits', 'Volume'], inplace=True, axis=1)
    a = a.assign(Delta=a['Close'].pct_change())
    appendedData = pd.concat([appendedData, pd.DataFrame(a)])
    #appendedData = appendedData.assign(Delta=appendedData[
    # 'Close'].pct_change())
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


# setting up our graph information
sns.set(font_scale=0.6)
fig, axes = plt.subplots(3, 3)
fig.suptitle('Equity Indices Historical Information')

# purpose is to create a number of figures reflecting data
fig0 = plt.figure()
all = sns.lineplot(ax=axes[0,0], data=appendedData, x='Date', y='Close',
                   hue='Ticker', linewidth=0.7, ci=None)

fig1 = plt.figure()
ixic = sns.lineplot(ax=axes[0,1], data=ixicOnly, x='Date', y='Close',
                    linewidth=0.7, ci=None)

fig2 = plt.figure()
rui = sns.lineplot(ax=axes[0,2], data=ruiOnly, x='Date', y='Close',
                   linewidth=0.7, ci=None)

fig3 = plt.figure()
rlv = sns.lineplot(ax=axes[1, 0], data=rlvOnly, x='Date', y='Close',
                   linewidth=0.7, ci=None)

fig4 = plt.figure()
rlg = sns.lineplot(ax=axes[2, 0], data=rlgOnly, x='Date', y='Close',
                   linewidth=0.7, ci=None)

fig5 = plt.figure()
rut = sns.lineplot(ax=axes[1, 2], data=rutOnly, x='Date', y='Close',
                   linewidth=0.7, ci=None)

fig6 = plt.figure()
ruj = sns.lineplot(ax=axes[1, 1], data=rujOnly, x='Date', y='Close',
                   linewidth=0.7, ci=None)

fig7 = plt.figure()
ruo = sns.lineplot(ax=axes[2, 1], data=ruoOnly, x='Date', y='Close',
                   linewidth=0.7, ci=None)

# some stylistic changes
for ax in fig.axes:
    ax.tick_params(labelrotation=90, axis='x')

filename = 'equityIndices.pdf'
save_multi_image(filename)

