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
materialsList = ['BHP', 'LIN', 'RIO', 'CTA-PB', 'SHW', 'APD', 'CTVA', 'FCX',
                 'NTR', 'ECL']

# topics we want to grab from info
topics = {'shortName'}

# processing our df
df_main = data_processor(list=materialsList, period='1Y')

# use this code snippet once
# df_main.to_csv('.\data_files\materials_data.csv', index=False)

# creating df list related to ticker symbol
bhp = df_main[df_main['Ticker'] == materialsList[0]]
lin = df_main[df_main['Ticker'] == materialsList[1]]
rio = df_main[df_main['Ticker'] == materialsList[2]]
cta_pb = df_main[df_main['Ticker'] == materialsList[3]]
shw = df_main[df_main['Ticker'] == materialsList[4]]
apd = df_main[df_main['Ticker'] == materialsList[5]]
ctva = df_main[df_main['Ticker'] == materialsList[6]]
fcx = df_main[df_main['Ticker'] == materialsList[7]]
ntr = df_main[df_main['Ticker'] == materialsList[8]]
ecl = df_main[df_main['Ticker'] == materialsList[9]]

# creating a list of our specific dfs
dfs = [bhp, lin, rio, cta_pb, shw, apd, ctva, fcx, ntr, ecl]

# creating our figures
visual_maker(ticker_list=materialsList, dfs=dfs)

# saving plots in pdf format
filename = '.\market_visuals\materials_visuals_'
save_multi_image(filename + currentDate + '.pdf')



