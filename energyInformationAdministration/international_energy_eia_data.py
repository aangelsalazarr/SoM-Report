import os  # allows us to access api key from our environment
import requests  # will be used make a https get request
import pandas as pd  # will be used to create dfs
import matplotlib.pyplot as plt  # will be used for visuals
from matplotlib import rc
import seaborn as sns  # used for plotting purposes
from pdfConverter import save_multi_image  # used to create pdf files
from datetime import date
from eia_data_processor import grab_eia_data
from eia_data_processor import is_float
from dateutil.relativedelta import relativedelta

# some params related to the framework of pdf output that we will need
rc('mathtext', default='regular')
plt.rcParams["figure.autolayout"] = True

# creating current date var
today = date.today()
currentDate = today.strftime('%m_%d_%y')
start_date = today - relativedelta(years=5)
eia_start_date = start_date.strftime('%Y-%m-%d')

# purpose is to store EIA API Key in a var
api_key = os.environ.get('eiaAPI')

# next, we want to store base url for international energy data
base_url = 'https://api.eia.gov/v2/international/data/' + "?api_key=" + str(
    api_key)

# laying out our X-Params which will be used in our HTTPS GET request
# notice we have: frequency, data, facets, start, end, sort, offset, etc.
# also notice that request length is limited to 5000
'''
X-Params: {
    "frequency": "monthly",
    "data": [
        "value"
    ],
    "facets": {},
    "start": null,
    "end": null,
    "sort": [
        {
            "column": "period",
            "direction": "desc"
        }
    ],
    "offset": 0,
    "length": 5000,
    "api-version": "2.0.2"
}
'''
# purpose is to convert data facet to be included in url
# layout: '&data[i]=item_i&data[i+1]=item_i+1...'
url_data_input = '&data[0]=value'
url_start_input = "&start=" + str(eia_start_date)  # not needed in our case
url_end_input = 0  # not needed in our case
url_freq_input = '&frequency=monthly'

# now we would like to concatenate all inputs into one main url
main_url = base_url + url_data_input + url_freq_input + url_start_input

df = grab_eia_data(url=main_url)

df = df[df['value'].apply(lambda x: is_float(x))]
# let's export our df into a csv file one time to store it and then comment out
# df.to_csv('.\data_csv_format\international_energy_data_eia.csv', index=False)

'''
Looking at the csv file, the following are the columns
- period, productId, productName, activity, activityName, countryRegionId, 
    countryRegionName, countryRegionTypeId, countryRegionTypeName, unit, 
    unitName, value

'''
# splitting df to include/exclude oecd data
value_list = ['NOEC', 'OEAO', 'OECD', 'OEEU', 'OENA', 'WP18', 'WP21',
              'WP22', 'WP23', 'WP24', 'WP26']
df_oecd = df[df['countryRegionId'].isin(value_list)]
df = df[~df['countryRegionId'].isin(value_list)]


# let's visualize some of our data now, beginning with period as x-axis and
# value as y axis. We will compartmentalize by activityName
fig1 = plt.figure()
visual_1 = sns.relplot(data=df[df['activityId'] == 1],
                       x='period', y='value',
                       col='productName', col_wrap=3,
                       # col='countryRegionName', col_wrap=10,
                       kind='line')

fig2 = plt.figure()
visual_2 = sns.lineplot(data=df[df['activityId'] == 2],
                        x='period',
                        y='value',
                        hue='countryRegionName').set(title='Refined Petro '
                                                     'Consumption')

fig3 = plt.figure()
visual_3 = sns.lineplot(data=df[df['activityId'] == 3],
                       x='period',
                       y='value',
                       hue='productName')

fig4 = plt.figure()
visual_4 = sns.lineplot(data=df[df['activityId'] == 5],
                       x='period',
                       y='value',
                       hue='countryRegionName').set(title='Petro Stocks')


# creating file name to output plots as pdf
filename = 'international_data_eia_'

# saving our graphs as a pdf
save_multi_image(filename + currentDate + '.pdf')

