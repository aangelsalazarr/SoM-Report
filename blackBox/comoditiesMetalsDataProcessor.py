import yfinance as yf

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
goldHistory = gold.info(period="1Y")
platinumHistory = platinum.info(period='1Y')
palladiumHistory = palladium.info(period='1Y')
silverHistory = silver.info(period='1Y')
copperHistory = lmeCu.info(period='1Y')
aluminumHistory = aluminum.info(period='1Y')

# commodities history list
commoditiesHistories = [goldHistory, platinumHistory, palladiumHistory,
                        silverHistory, copperHistory, aluminumHistory]


