import pandas as pd
import seaborn as sns
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

# creating a list of tickey symbols we want to pull from the yfinance api
comsList = ['GOOGL', 'META', 'DIS', 'TMUS', 'VZ', 'CMCSA', 'NFLX', 'T', 'ATVI',
            'AMX']

# tppic we want to grab from info
topics = {'shortName'}

# process to grab historical data and transform it
df_main = data_processor(list=comsList, period='1Y')

# use this code snippet once
# df_main.to_csv('.\data_csv_format\comms_data.csv', index=False)

# creating firm specific dfs to use in out visual creation
google = df_main[df_main['Ticker'] == comsList[0]]
meta = df_main[df_main['Ticker'] == comsList[1]]
disney = df_main[df_main['Ticker'] == comsList[2]]
tmobile = df_main[df_main['Ticker'] == comsList[3]]
verizon = df_main[df_main['Ticker'] == comsList[4]]
comcast = df_main[df_main['Ticker'] == comsList[5]]
netflix = df_main[df_main['Ticker'] == comsList[6]]
att = df_main[df_main['Ticker'] == comsList[7]]
activision = df_main[df_main['Ticker'] == comsList[8]]
americaMovil = df_main[df_main['Ticker'] == comsList[9]]

# creating our list of specific dfs
dfs = [google, meta, disney, tmobile, verizon, comcast, netflix, att,
       activision, americaMovil]

# creating figures
visual_maker(list=dfs)

# saving plots in pdf format
filename = 'comms_visuals_'
save_multi_image(filename + currentDate + '.pdf')


