import null as null
import requests
import os
from datetime import date
from dateutil.relativedelta import relativedelta

'''
Purpose of this is to grab relevant price data on the electricity market in the
USA
'''

# first we want to retrieve our api key and make sure it is good to go
apiKey = os.environ.get('eiaAPI')

# api endpoint; will be adding specifics at the end of URL
URL = "https://api.eia.gov/v2/electricity/"

# here are the specifics of what we are looking for
specificReq = "electricity/retail-sales/data/"

# electricity pricing API endpoint
electricityPrices = URL + specificReq

'''
here we are setting up our time range, overall we should not worry about the end
year because if left as null it is assumed it will grab the most recent
data. however, we do not want to go back so many decades so we will limit to
going back 5 years max
'''
currentDate = date.today()
startDate = currentDate - relativedelta(years=5)
startDateEIA = startDate.strftime("%Y-%m")


# purpose is to define parameters
PARAMS = {
    'frequency': 'monthly',
    'data': [
        'customers', 'price', 'revenue', 'sales'
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