import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns
from matplotlib import rc
from black_box.pdfConverter import save_multi_image

rc('mathtext', default='regular')

# plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

"""
purpose is to intake a list of commodities and run a process of grabbing
historical data, parsing through the information, and visualizing the
information. best case scenario, we create a process where we input a list of
commodities and a pdf report is created presenting all the relevant graphs
"""

# metals futures that can be access via yahoofinance
gold = yf.Ticker("GC=F")
platinum = yf.Ticker("PL=F")
palladium = yf.Ticker("PA=F")
silver = yf.Ticker("SI=F")
lmeCu = yf.Ticker("HG=F")
aluminum = yf.Ticker("ALI=F")

# need to convert to .history to grab historical data
goldHistory = gold.history(period="1Y")
platinumHistory = platinum.history(period='1Y')
palladiumHistory = palladium.history(period='1Y')
silverHistory = silver.history(period='1Y')
copperHistory = lmeCu.history(period='1Y')
aluminumHistory = aluminum.history(period='1Y')

# commodities history list
commoditiesHistories = [goldHistory, platinumHistory, palladiumHistory,
                        silverHistory, copperHistory, aluminumHistory]

# create a for loop to clean the data
for commodity in commoditiesHistories:
    commodity.reset_index(inplace=True)
    commodity.drop(['Dividends', 'Stock Splits'], inplace=True, axis=1)

# now we will create multiple figures and put them into one pdf
fig1 = plt.figure()
golda = sns.lineplot(data=goldHistory, x='Date', y='Open',
                     color='green').set(title=gold.info['shortName'])
ax2_1 = plt.twinx()
goldb = sns.lineplot(data=goldHistory, x='Date', y='Volume', color='lightgreen')

fig2 = plt.figure()
platinuma = sns.lineplot(data=platinumHistory, x='Date', y='Open',
                    color='green').set(
    title=platinum.info['shortName'])
ax2_2 = plt.twinx()
platinumb = sns.lineplot(data=platinumHistory, x='Date', y='Volume',
                  color='lightgreen')

fig3 = plt.figure()
palladiuma = sns.lineplot(data=palladiumHistory, x='Date', y='Open',
                   color='green').set(
    title=palladium.info['shortName'])
ax2_3 = plt.twinx()
palladiumb = sns.lineplot(data=palladiumHistory, x='Date', y='Volume',
                 color='lightgreen')

fig4 = plt.figure()
silvera = sns.lineplot(data=silverHistory, x='Date', y='Open',
                      color='green').set(
    title=silver.info['shortName'])
ax2_4 = plt.twinx()
silverb = sns.lineplot(data=silverHistory, x='Date', y='Volume',
                    color='lightgreen')

fig5 = plt.figure()
coppera = sns.lineplot(data=copperHistory, x='Date', y='Open',
                      color='green').set(
    title=lmeCu.info['shortName'])
ax2_5 = plt.twinx()
copperb = sns.lineplot(data=copperHistory, x='Date', y='Volume',
                    color='lightgreen')

fig6 = plt.figure()
aluminuma = sns.lineplot(data=aluminumHistory, x='Date', y='Open',
                    color='green').set(
    title=aluminum.info['shortName'])
ax2_6 = plt.twinx()
aluminumb = sns.lineplot(data=aluminumHistory, x='Date', y='Volume',
                  color='lightgreen')


filename = '.\data_files\CommoditiesFuturesInformation.pdf'
save_multi_image(filename)
