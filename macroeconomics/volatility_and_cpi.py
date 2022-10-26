import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os
from black_box.bls_data_processor import fetch_bls_series
import seaborn as sns
from datetime import datetime
import datetime
from matplotlib import rc
from matplotlib.backends.backend_pdf import PdfPages
from black_box.pdfConverter import save_multi_image
from black_box.yfinance_data_processor import data_processor

rc('mathtext', default='regular')
plt.rcParams["figure.autolayout"] = True

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

vix_df = data_processor(list=["^VIX"], period='ytd')

# ______________________________________________________________________________
# BLS API DATA FROM HERE AND DOWN
# grabbing data from bls public api
# we want to grab the bls from our virtual environment
bls_api_key = os.environ.get('blsAPI')

# series id of interest
unemployment_rate = "LNS14000000"
cpi = "CUUR0000SA0"  # consumer price index
eci = "CIU1010000000000A"  # employment cost index
imports = "EIUIR"  # imports all commodities
exports = "EIUIQ"  # exports, all commodities

# setting up our series list
series = [unemployment_rate, cpi, imports, exports]

# grabbing bls api data
blsMainDF = fetch_bls_series(series=series)

'''
Looking at our bls data structure we see the following:
*level 1: 
- {4 props}
**Level 2: 
- status:
- responseTime
- message
- Results
***Level 3 [Results unnest]:
- series
    - 0
        - seriesID:
        - data:
            - 0:
                - year
                - period
                -periodName
                -latest
                - value
            - 1:
            - ...
            - M
    - 1
    - ...
    - N
    
So it seems that we only care about first grabbing props in series which 
each index contains specific information requested. for instance, if we req
5 series id, then N = 5. best way to move forward would be to allocate a df 
for each series index, grab seriesID and add it to a df that grabbed data per
series index. once we have N df's, then given they are similar in structure, we
just need to vertically concatenate them and there we have 1 master df.
'''

# visuals for
sns.set(font_scale=0.7)
fig, axes = plt.subplots(2, 2)
fig.suptitle('U.S. Bureau of Labor Statistics Insights')

# setting our specific data
unemployment = blsMainDF[blsMainDF['seriesID'] == 'LNS14000000']

fig5 = plt.figure()
vixOpen = sns.lineplot(data=vix_df['Open'], color='blue')
ax2 = plt.twinx()
vixChange = sns.lineplot(data=vix_df['Delta'], color='lightgreen',
                     ax=ax2)


fig1 = sns.lineplot(ax=axes[0, 0], data=unemployment, x='Date',
                    y='value', linewidth=0.7, ci=None).set(title='Unemployment')

fig2 = sns.lineplot(ax=axes[0, 1], data=blsMainDF[blsMainDF['seriesID'] ==
                                                  'CUUR0000SA0'], x='Date',
                    y='value', linewidth=0.7, ci=None).set(title='CPI')

fig3 = sns.lineplot(ax=axes[1, 0], data=blsMainDF[blsMainDF['seriesID'] ==
                                                  'EIUIR'], x='Date',
                    y='value', linewidth=0.7, ci=None).set(title='Imports, '
                                                                 'All '
                                                                 'Commodities')

fig4 = sns.lineplot(ax=axes[1, 1], data=blsMainDF[blsMainDF['seriesID'] ==
                                                  'EIUIQ'], x='Date',
                    y='value', linewidth=0.7, ci=None).set(title='Exports, '
                                                                 'All '
                                                                 'Commodities')

for ax in fig.axes:
    ax.tick_params(labelrotation=90, axis='x')


blsMainDF.to_csv('./data_files/cpi_data.csv', index=False)
vix_df.to_csv('./data_files/volatility_data.csv', index=False)

filename = './data_visuals/volatility_and_cpi_visuals.pdf'
save_multi_image(filename)
