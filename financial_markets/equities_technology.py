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

# creating a list of ticker symbols we want to pull from yfinance api
techList = ['AAPL', 'MSFT', 'TSM', 'NVDA', 'ORCL', 'ASML', 'AVGO', 'CSCO',
            'ACN', 'CRM']

# topics we want to grab from info
topics = {'shortName'}

# processing our df
df_main = data_processor(list=techList, period='1Y')

# use this code snippet once
df_main.to_csv('.\data_csv_format\market_tech_data.csv', index=False)

# creating df list related to ticker symbol
a = df_main[df_main['Ticker'] == techList[0]]
b = df_main[df_main['Ticker'] == techList[1]]
c = df_main[df_main['Ticker'] == techList[2]]
d = df_main[df_main['Ticker'] == techList[3]]
e = df_main[df_main['Ticker'] == techList[4]]
f = df_main[df_main['Ticker'] == techList[5]]
g = df_main[df_main['Ticker'] == techList[6]]
h = df_main[df_main['Ticker'] == techList[7]]
i = df_main[df_main['Ticker'] == techList[8]]
j = df_main[df_main['Ticker'] == techList[9]]

# creating a list of our specific dfs
dfs = [a, b, c, d, e, f, g, h, i, j]

# creating our figures
visual_maker(ticker_list=techList, dfs=dfs)

# saving plots in pdf format
filename = '.\market_visuals\market_tech_visuals_'
save_multi_image(filename + currentDate + '.pdf')

