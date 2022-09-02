# purpose of this file is to grab data on the top 10 energy companies in the
# equities market
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# exxon mobil coroporation
exxon = yf.Ticker("XOM")

# chevron corporation
chevron = yf.Ticker("CVX")

# shell plc
shell = yf.Ticker("SHEL")

# conocophillips
conoco = yf.Ticker("COP")

# petrochina company limited
petrochina = yf.Ticker("PTR")

# total energy se
totalEnergy = yf.Ticker("TTE")

# equinor asa
equinor = yf.Ticker("EQNR")

# bp plc
bp = yf.Ticker("BP")

# petroleo brasileiro S.A - petrobas
petroBrasil = yf.Ticker("PBR")

# enbridge inc
enbridge = yf.Ticker("ENB")

# combining all energy related stocks into a list
energyMarketList = [exxon, chevron, shell, conoco, petrochina, totalEnergy,
                    equinor, bp, petroBrasil, enbridge]

# now we will find topics of interest aka data that we want to grab
energyTopics = {
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

