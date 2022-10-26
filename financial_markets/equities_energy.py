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

# now we will find topics of interest aka data that we want to grab
topics = {
    'fullTimeEmployees', 'ebitdaMargins', 'profitMargins', 'grossMargins',
    'operatingCashflow', 'revenueGrowth', 'operatingMargins', 'ebitda',
    'targetLowPrice', 'recommendationKey', 'grossProfits', 'freeCashflow',
    'targetMedianPrice', 'currentPrice', 'earningsGrowth', 'currentRatio',
    'returnOnAssets', 'targetMeanPrice', 'debtToEquity', 'returnOnEquity',
    'targetHighPrice', 'totalCash', 'totalDebt', 'totalRevenue',
    'totalCashPerShare', 'revenuePerShare', 'quickRatio', 'recommendationMean',
    'shortName', 'enterpriseToRevenue', 'enterpriseToEbitda', '52WeekChange',
    'forwardEps', 'sharesOutstanding', 'bookValue', 'sharesShort',
    'sharesPercentSharesOut', 'lastFiscalYearEnd', 'heldPercentInstitution',
    'netIncomeToCommon', 'trailingEps', 'lastDividendValue',
    'SandP52WeekChange',  'priceToBook', 'heldPercentInsiders',
    'nextFiscalYearEnd', 'mostRecentQuarter', 'shortRatio',
    'sharesShortPreviousMonthDate', 'floatShares', 'beta', 'enterpriseValue',
    'lastDividendDate', 'earningsQuarterlyGrowth',
    'priceToSalesTrailing12Months', 'dateShortInterest', 'forwardPE',
    'shortPercentOfFloat', 'sharesShortPriorMonth', 'previousClose',
    'regularMarketOpen', 'twoHundredDayAverage', 'trailingAnnualDividendYield',
    'payoutRatio', 'volume24Hr', 'regularMarketDayHigh',
    'averageDailyVolume10Day', 'regularMarketPreviousClose', 'fiftyDayAverage',
    'trailingAnnualDividendRate', 'open', 'averageVolume10Days',
    'dividendRate', 'regularMarketDayLow', 'trailingPE', 'regularMarketVolume',
    'marketCap', 'averageVolume', 'dayLow', 'ask', 'askSize', 'volume',
    'fiftyTwoWeekHigh', 'fiveYearAvgDividendYield', 'fiftyTwoWeekLow', 'bid',
    'dividendYield', 'bidSize', 'dayHigh', 'regularMarketPrice',
    'preMarketPrice', 'trailingPegRatio',
}

# creating a list of ticker symbols we want to pull from yfinance api
energyList = ['XOM', 'CVX', 'SHEL', 'COP', 'TTE', 'EQNR', 'BP', 'PBR',
              'EOG', 'ENB', 'SLB', 'CNQ', 'OXY', 'PXD', 'MPC', 'BKR',
              'NEE']

# processing our df
df_main = data_processor(list=energyList, period='1Y')

# run this code snippet once
df_main.to_csv('.\data_csv_format\energy_data.csv', index=False)

# creating a list related to ticker symbol
xom = df_main[df_main['Ticker'] == energyList[0]]
cvx = df_main[df_main['Ticker'] == energyList[1]]
shel = df_main[df_main['Ticker'] == energyList[2]]
cop = df_main[df_main['Ticker'] == energyList[3]]
tte = df_main[df_main['Ticker'] == energyList[4]]
eqnr = df_main[df_main['Ticker'] == energyList[5]]
bp = df_main[df_main['Ticker'] == energyList[6]]
pbr = df_main[df_main['Ticker'] == energyList[7]]
eog = df_main[df_main['Ticker'] == energyList[8]]
enb = df_main[df_main['Ticker'] == energyList[9]]
slb = df_main[df_main['Ticker'] == energyList[10]]
cnq = df_main[df_main['Ticker'] == energyList[11]]
oxy = df_main[df_main['Ticker'] == energyList[12]]
pxd = df_main[df_main['Ticker'] == energyList[13]]
mpc = df_main[df_main['Ticker'] == energyList[14]]
bkr = df_main[df_main['Ticker'] == energyList[15]]
nee = df_main[df_main['Ticker'] == energyList[16]]

# creating a list of our specific dfs
dfs = [xom, cvx, shel, cop, tte, eqnr, bp, pbr, eog, enb, slb, cnq, oxy, pxd,
       mpc, bkr, nee]

# creating our figures
visual_maker(ticker_list=energyList, dfs=dfs)

# saving plots in pdf format
filename = '.\market_visuals\energy_visuals_'
save_multi_image(filename + currentDate + '.pdf')





