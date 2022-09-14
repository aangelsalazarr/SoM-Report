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
equityIndices = ['^SPX', '^IXIC', '^RUI', '^RLV', '^RLG', '^RUT', '^RUJ',
                 '^RUO']

indexValue = 0
# create a empty dataframe
appendedData = pd.DataFrame(columns=['Index'])

# process to grab historical data
for index in equityIndices:
    a = yf.Ticker(str(index)).history(period="1Y")
    a.reset_index(inplace=True)
    a.drop(['Dividends', 'Stock Splits', 'Volume'], inplace=True, axis=1)
    appendedData.append(a)
    if appendedData['Index'].isnull:
        appendedData['Index'].fillna(index, inplace=True)
    else:
        continue

# combining all of our dfs into 1 df
# appendedData = pd.concat(appendedData)

# want to initialize  multiple ticker objects
# tickersList = '^SPX ^IXIC ^RUI ^RLV ^RLG ^RUT ^RUJ ^RUO'
# tickers = yf.Tickers(tickersList)

# access all of the datas historical data
# equityIndicesHistData = tickers.history(period="1Y")

# cleaning up our data
#equityIndicesHistData.reset_index(inplace=True)
#equityIndicesHistData.drop(['Dividends', 'Stock Splits', 'Volume'],
                           #inplace=True,
                           #axis=1)

# checkin our df
print(appendedData)

# exporting out data as a csv file
# equityIndicesHistData.to_csv('equityIndicesHistData.csv', index=False)

'''
at this point we want to create a number of figures that provides us with 
insights on the historical data we have now collected 
'''

'''
# purpose is to create a number of figures reflecting data
fig1 = plt.figure()
nasdaq = sns.lineplot(data=equityIndicesHistData, x='Date', y='Close')

fig2 = plt.figure()
russell1 = sns.lineplot(data=equityIndicesHistData, )

fig3 = plt.figure()
russellValue1 = sns.lineplot(data=equityIndicesHistData, )

fig4 = plt.figure()
russellGrowth1 = sns.lineplot(data=equityIndicesHistData, )

fig5 = plt.figure()
russell2 = sns.lineplot(data=equityIndicesHistData, )

fig6 = plt.figure()
russellValue2 = sns.lineplot(data=equityIndicesHistData, )

fig7 = plt.figure()
russellGrowth2 = sns.lineplot(data=equityIndicesHistData, )

fig8 = plt.figure()
sandp = sns.lineplot()
'''