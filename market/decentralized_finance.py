import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pdfConverter import save_multi_image
from matplotlib import rc
from yfinance_data_processor import data_processor
from datetime import date

#
rc('mathtext', default='regular')
plt.rcParams["figure.autolayout"] = True
pd.set_option('display.max_columns', None)

# time related stuff
today = date.today()
currentDate = today.strftime('%m_%d_%y')

'''
The purpose of this file is to grab data related to the top 5 cryptocurrencies
and create visualizations that are helpful in getting a sense of what is going
on. Looking at the following cryptos:
    - Bitcoin, Ethereum, Tether, USD Coin, BNB
We would also like to compare the 5 to other indexes in the market and sector
'''
# creating list of ticker symbols we want to pull from yahoofinance api
cryptoList = ['BTC-USD', 'ETH-USD', 'USDT-USD', 'USDC-USD', 'BNB-USD']

# what we want to grab from info
topics = {'shortName'}

# process to grab historical data and transform it
df_main = data_processor(list=cryptoList, period='1Y')

# storing our now transformed data into a csv file to reference in future
# only necessary to run this code snippet once
# df.to_csv('.\data_csv_format\defi_data.csv', index=False)

# setting params for data and creating sub dfs
sns.set(font_scale=0.5)
sns.set_style('dark')
btc = df_main[df_main['Ticker'] == 'BTC-USD']
eth = df_main[df_main['Ticker'] == 'ETH-USD']
usdt = df_main[df_main['Ticker'] == 'USDT-USD']
usdc = df_main[df_main['Ticker'] == 'USDC-USD']
bnb = df_main[df_main['Ticker'] == 'BNB-USD']

# various lists to include in automated visualizer
dfs = [btc, eth, usdt, usdc, bnb]

# used to iterate through crypto list
count = 0

for df in dfs:
    fig, axes = plt.subplots(2, 3)
    fig.suptitle(cryptoList[count])

    sns.lineplot(ax=axes[0, 0], data=df, x='Date', y='Close',
                 linewidth=0.5, color='maroon')
    sns.lineplot(ax=axes[0, 1], data=df, x='Date', y='Volume',
                 linewidth=0.5, color='maroon')
    sns.lineplot(ax=axes[0, 2], data=df, x='Date', y='volumeDelta',
                 linewidth=0.5, color='maroon')
    sns.lineplot(ax=axes[1, 0], data=df, x='Date', y='high_low_delta',
                 linewidth=0.5, color='maroon')
    sns.lineplot(ax=axes[1, 1], data=df, x='Date', y='end_day_delta',
                 linewidth=0.5, color='maroon')
    sns.lineplot(ax=axes[1, 2], data=df, x='Date', y='Delta',
                 linewidth=0.5, color='maroon')

    # rotating period access
    for ax in fig.axes:
        ax.tick_params(labelrotation=90, axis='x')
        ax.set(xlabel=None)

    count += 1


# saving plots in pdf format
filename = 'defi_visuals_'
save_multi_image(filename + currentDate + '.pdf')
