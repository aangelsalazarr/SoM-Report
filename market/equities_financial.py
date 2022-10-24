import pandas as pd
import matplotlib.pyplot as plt
from pdfConverter import save_multi_image
from matplotlib import rc
from yfinance_data_processor import data_processor
from yfinance_visual_processor import visual_maker
from datetime import date

# parameter set up
rc('mathtext', default='regular')
plt.rcParams['figure.autolayout'] = True
pd.set_option('display.max_columns', None)

# time related code
today = date.today()
currentDate = today.strftime('%m_%d_%y')

# creating a list of ticker symboles we want to pull from yfinance api
financialList = ['BRK-A', 'BRK-B', 'JPM', 'V', 'BAC', 'MA', 'WFC', 'C',
                 'MS', 'SCHW', 'GS', 'BX', 'BLK', 'UBS', 'CME']

# topics we want to grab from info
topics = {'shortName'}

# processing our df
df_main = data_processor(list=financialList, period='1Y')

# run this code only once
df_main.to_csv('.\data_csv_format\market_financials_data.csv', index=False)

# creating a list of related ticker symbols
brk_a = df_main[df_main['Ticker'] == financialList[0]]
brk_b = df_main[df_main['Ticker'] == financialList[1]]
jpm = df_main[df_main['Ticker'] == financialList[2]]
v = df_main[df_main['Ticker'] == financialList[3]]
bac = df_main[df_main['Ticker'] == financialList[4]]
ma = df_main[df_main['Ticker'] == financialList[5]]
wfc = df_main[df_main['Ticker'] == financialList[6]]
c = df_main[df_main['Ticker'] == financialList[7]]
ms = df_main[df_main['Ticker'] == financialList[8]]
schw = df_main[df_main['Ticker'] == financialList[9]]
gs = df_main[df_main['Ticker'] == financialList[10]]
bx = df_main[df_main['Ticker'] == financialList[11]]
blk = df_main[df_main['Ticker'] == financialList[12]]
ubs = df_main[df_main['Ticker'] == financialList[13]]
cme = df_main[df_main['Ticker'] == financialList[14]]

# creating a list of our specific dfs
dfs = [brk_a, brk_b, jpm, v, bac, ma, wfc, c, ms, schw, gs, bx, blk, ubs, cme]

# creating our figures
visual_maker(ticker_list=financialList, dfs=dfs)

# saving plots in pdf format
filename = '.\market_visuals\market_financial_visuals_'
save_multi_image(filename + currentDate + '.pdf')

