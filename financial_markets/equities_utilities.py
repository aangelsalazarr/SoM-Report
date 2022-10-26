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
utilitiesList = ['NEE', 'SO', 'DUK', 'D', 'SRE', 'AEP', 'NGG', 'EXC', 'PCG',
                 'XEL']

# topics we want to grab from info
topics = {}

# processing data request into df
df_main = data_processor(list=utilitiesList, period='1Y')

# use this code snippet once
# df_main.to_csv('.\data_files\market_utilities_data.csv', index=False)

# creating df list related to ticker symbol
nee = df_main[df_main['Ticker'] == utilitiesList[0]]
so = df_main[df_main['Ticker'] == utilitiesList[1]]
duk = df_main[df_main['Ticker'] == utilitiesList[2]]
d = df_main[df_main['Ticker'] == utilitiesList[3]]
sre = df_main[df_main['Ticker'] == utilitiesList[4]]
aep = df_main[df_main['Ticker'] == utilitiesList[5]]
ngg = df_main[df_main['Ticker'] == utilitiesList[6]]
exc = df_main[df_main['Ticker'] == utilitiesList[7]]
pcg = df_main[df_main['Ticker'] == utilitiesList[8]]
xel = df_main[df_main['Ticker'] == utilitiesList[9]]

# creating a list of our specific dfs
dfs = [nee, so, duk, d, sre, aep, ngg, exc, pcg, xel]

# creating our figures
visual_maker(ticker_list=utilitiesList, dfs=dfs)

# saving plots in pdf format
filename = '.\market_visuals\market_utilities_visuals_'
save_multi_image(filename + currentDate + '.pdf')