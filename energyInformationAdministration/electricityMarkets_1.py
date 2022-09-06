import null as null
import requests
import os
from datetime import date
from dateutil.relativedelta import relativedelta
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

'''
Purpose of this is to grab relevant price data on the electricity market in the
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
facetsInput= "&facets[sectorid][0]=ALL&facets[sectorid][1]=COM&facets[" \
             "sectorid][2]=IND&facets[sectorid][3]=OTH&facets[" \
             "sectorid][4]=RES&facets[" \
             "sectorid][5]=TRA"
frequencyInput = "&frequency=monthly"
endDateInput = "&start=" + str(startDateEIA)

# adding everything up
electricityPricesURL = electricityPricesURL + dataInput + facetsInput \
                       +frequencyInput + endDateInput

# helping us visualize our url
# print(electricityPricesURL)

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

# sending get request and saving the response as a response object
r = requests.get(url=electricityPricesURL)

# extracting data in json format
data = r.json()

# grabbing only data object
entries = data['response']["data"]

# converting our json data format to pandas
df = pd.DataFrame(data=entries)
df2 = df[df['stateid'] != 'US']

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
fig1 = sns.barplot(data=df2, x='stateDescription', y='customers',
                   order = df2.sort_values('customers',
                                           ascending=False).stateDescription)
fig1.set_xticklabels(fig1.get_xticklabels(), rotation=90)
plt.show()

