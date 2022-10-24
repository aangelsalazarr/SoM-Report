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
healthcareList = ['UNH', 'JNJ', 'LLY', 'ABBV', 'PFE', 'MRK', 'NVO', 'TMO',
                  'DHR', 'AZN']

# topics we want to grab from info
topics = {'shortName'}

# processing our df
df_main = data_processor(list=healthcareList, period='1Y')

# use this code snippet once
df_main.to_csv('.\data_csv_format\healthcare_data.csv', index=False)

# creating df list related to ticker symbol
unh = df_main[df_main['Ticker'] == healthcareList[0]]
jnj = df_main[df_main['Ticker'] == healthcareList[1]]
lly = df_main[df_main['Ticker'] == healthcareList[2]]
abbv = df_main[df_main['Ticker'] == healthcareList[3]]
pfe = df_main[df_main['Ticker'] == healthcareList[4]]
mrk = df_main[df_main['Ticker'] == healthcareList[5]]
nvo = df_main[df_main['Ticker'] == healthcareList[6]]
tmo = df_main[df_main['Ticker'] == healthcareList[7]]
dhr = df_main[df_main['Ticker'] == healthcareList[8]]
azn = df_main[df_main['Ticker'] == healthcareList[9]]

# creating a list of our specific dfs
dfs = [unh, jnj, abbv, pfe, mrk, nvo, tmo, dhr, azn]

# creating our figures
visual_maker(ticker_list=healthcareList, dfs=dfs)

# saving plots in pdf format
filename = '.\market_visuals\healthcare_visuals_'
save_multi_image(filename + currentDate + '.pdf')

