import null as null
import requests
import os
from datetime import date
from dateutil.relativedelta import relativedelta
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rc
from black_box.pdfConverter import save_multi_image
from black_box.eia_data_processor import grab_eia_data

rc('mathtext', default='regular')

plt.rcParams["figure.autolayout"] = True

pd.set_option('display.max_columns', None)

'''
Purpose of this is to grab relevant price data on the electricity financial_markets in the
USA
'''

# first we want to retrieve our api key and make sure it is good to go
apiKey = os.environ.get('eiaAPI')

'''
here we are setting up our time range, overall we should not worry about the end
year because if left as null it is assumed it will grab the most recent
data. however, we do not want to go back so many decades so we will limit to
going back 5 years max
'''
currentDate = date.today()
startDate = currentDate - relativedelta(years=5)
startDateEIA = startDate.strftime("%Y-%m-%d")

# api endpoint; will be adding specifics at the end of URL
URL = "https://api.eia.gov/v2/"

# here are the specifics of what we are looking for
specificReq = "electricity/retail-sales/data"

# electricity pricing API endpoint
electricityPricesURL = URL + specificReq + "?api_key=" + str(apiKey)

"""
it is proving difficult at the moment to use HTTPS header so we will look at our
PARAMS and slowly convert it and add it to our url since our case is specific
in this python script
"""

dataInput = "&data[0]=customers&data[1]=price&data[2]=revenue&data[3]=sales"
facetsInput = "&facets[sectorid][0]=ALL&facets[sectorid][1]=COM&facets[" \
              "sectorid][2]=IND&facets[sectorid][3]=OTH&facets[" \
              "sectorid][4]=RES&facets[" \
              "sectorid][5]=TRA"
freq_input = "&frequency=monthly"
start_input = "&start=" + str(startDateEIA)

# adding everything up
electricityPricesURL = electricityPricesURL + dataInput + facetsInput \
                       + freq_input + start_input


# purpose is to define parameters
PARAMS = {
    'frequency': 'monthly',
    'data': [
        "customers", "price", "revenue", "sales"
    ],
    'facets': {
        'sectorid': [
            'ALL', 'COM', 'IND', 'OTH', 'RES', 'TRA'
        ]
    },
    'start': startDateEIA,
    'end': null,
    'sort': [
        {
            'column': 'period',
            'direction': 'desc'
        }
    ],
    'offset': 0,
    'length': 5000,
    'api-version': '2.0.2'
}

# processing into df
df = grab_eia_data(url=electricityPricesURL)

# outputting df as csv file
df.to_csv('.\data_files\electricity_prices_us.csv')

'''
Let it be noted that the entries contains all the data that we need and has the
following columns: 
- period
- statid
- stateDescription
- sectorid
- sectorName
- customers
- price
- revenue
- sales
- customer-units
- price-units
- revenue-units
- sales-units
'''

# let's look at a quick plot of stateDescription and customers (bar graph)
# how to sort values but takes a long time lol
# order = df2.sort_values('customers', ascending=False).stateDescription
# add in .barplot params

"""
now, we want to grab all of the data and start creating graphs, the first will 
be related to customers and price by sector (there will be 6 plots)
"""
sns.set(font_scale = 0.3)
fig, axes = plt.subplots(2, 3)
fig.suptitle('U.S. Electricity Price by Sector')

fig1 = sns.lineplot(ax=axes[0, 0], data=df[df['sectorid'] == 'ALL'],
                    x='period', y='price', linewidth= 0.7,
                    ci=None).set(title='All Sectors (Average)')  # total

fig2 = sns.lineplot(ax=axes[0, 1], data=df[df['sectorid'] == 'COM'],
                    x='period', y='price', linewidth= 0.7,
                    ci = None).set(title='Commercial')  #
# commercial

fig3 = sns.lineplot(ax=axes[0, 2], data=df[df['sectorid'] == 'IND'],
                    x='period', y='price', linewidth= 0.7,
                    ci = None).set(title='Industrial')  # industrial

fig4 = sns.lineplot(ax=axes[1, 0], data=df[df['sectorid'] == 'RES'],
                    x='period', y='price', linewidth= 0.7,
                    ci = None).set(title='Residential')  # residential

fig5 = sns.lineplot(ax=axes[1, 1], data=df[df['sectorid'] == 'TRA'],
                    x='period', y='price', linewidth= 0.7,
                    ci = None).set(title='Transportation')  # transportation

fig6 = sns.lineplot(ax=axes[1, 2], data=df, x='period', y='price',
                       hue='sectorid', linewidth= 0.7,
                    ci = None).set(title='All Sectors Split')  # all

# rotating period access
for ax in fig.axes:
  ax.set_ylabel(df['price-units'][0])
  ax.tick_params(labelrotation=90, axis='x')

'''
fig1 = sns.barplot(data=df2, x='stateDescription', y='customers')
fig1.set_xticklabels(fig1.get_xticklabels(), rotation=90)

fig2 = sns.lineplot(data=df2, x='sectorName', y='sales')
fig2.set_xticklabels(fig2.get_xticklabels(), rotation=90)
'''

filename = './data_visuals/eia_USElectricityPriceBySector.pdf'
save_multi_image(filename)

