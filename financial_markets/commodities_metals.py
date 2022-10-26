import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns
from matplotlib import rc
from black_box.pdfConverter import save_multi_image
from black_box.yfinance_data_processor import data_processor

rc('mathtext', default='regular')

# plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

"""
purpose is to intake a list of commodities and run a process of grabbing
historical data, parsing through the information, and visualizing the
information. best case scenario, we create a process where we input a list of
commodities and a pdf report is created presenting all the relevant graphs
"""

metals_list = ['GC=F', 'PL=F', 'PA=F', 'SI=F', 'HG=F', 'ALI=F']
metals_names = ['gold', 'platinum', 'palladium', 'silver', 'copper', 'aluminum']

# requesting list historical data
df_main = data_processor(list=metals_list, period='ytd')

# printing out df as csv
df_main.to_csv('.\data_files\commodities_metals_hist_data.csv', index=False)

# sub dfs
gold = df_main[df_main['Ticker'] == metals_list[0]]
platinum = df_main[df_main['Ticker'] == metals_list[1]]
palladium = df_main[df_main['Ticker'] == metals_list[2]]
silver = df_main[df_main['Ticker'] == metals_list[3]]
copper = df_main[df_main['Ticker'] == metals_list[4]]
aluminum = df_main[df_main['Ticker'] == metals_list[5]]

# now we will create multiple figures and put them into one pdf
fig1 = plt.figure()
golda = sns.lineplot(data=gold, x='Date', y='Open',
                     color='green').set(title='Gold')
ax2_1 = plt.twinx()
goldb = sns.lineplot(data=gold, x='Date', y='Volume', color='lightgreen')

fig2 = plt.figure()
platinuma = sns.lineplot(data=platinum, x='Date', y='Open',
                    color='green').set(
    title='Platinum')
ax2_2 = plt.twinx()
platinumb = sns.lineplot(data=platinum, x='Date', y='Volume',
                  color='lightgreen')

fig3 = plt.figure()
palladiuma = sns.lineplot(data=palladium, x='Date', y='Open',
                   color='green').set(
    title='Palladium')
ax2_3 = plt.twinx()
palladiumb = sns.lineplot(data=palladium, x='Date', y='Volume',
                 color='lightgreen')

fig4 = plt.figure()
silvera = sns.lineplot(data=silver, x='Date', y='Open',
                      color='green').set(
    title='silver')
ax2_4 = plt.twinx()
silverb = sns.lineplot(data=silver, x='Date', y='Volume',
                    color='lightgreen')

fig5 = plt.figure()
coppera = sns.lineplot(data=copper, x='Date', y='Open',
                      color='green').set(
    title='copper')
ax2_5 = plt.twinx()
copperb = sns.lineplot(data=copper, x='Date', y='Volume',
                    color='lightgreen')

fig6 = plt.figure()
aluminuma = sns.lineplot(data=aluminum, x='Date', y='Open',
                    color='green').set(
    title='aluminum')
ax2_6 = plt.twinx()
aluminumb = sns.lineplot(data=aluminum, x='Date', y='Volume',
                  color='lightgreen')


filename = '.\data_visuals\CommoditiesFuturesInformation.pdf'
save_multi_image(filename)
