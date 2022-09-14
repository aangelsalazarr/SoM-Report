import pandas as pd
import seaborn as sns
import os
import yfinance as yf
import matplotlib.pyplot as plt
import dataframe_image as dfi
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
    a = yf.Ticker(str(index)).history(period="1Y")
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

# purpose is to create a number of figures reflecting data
fig1 = plt.figure()
allDelta = sns.lineplot(data=appendedData, x='Date', y='Delta', hue='Ticker')

plt.show()

