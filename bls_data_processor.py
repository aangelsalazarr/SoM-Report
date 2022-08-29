# purpose is to grab data form bls public api
# this pyscript will be used ot create functions

import requests
import json
import os
import pandas as pd
from datetime import datetime
import datetime

# api key and end point
bls_api_key = os.environ.get('blsAPI')
bls_endpoint = "https://api.bls.gov/publicAPI/v2/timeseries/data/"

# out general defn
def fetch_bls_series(series, **kwargs):
    """
    pass in a list of BLS timeseries to fetch data and return the series
    in JSON format. Args can also be provided as kwargs:
    - start year
    - end year
    - catalog (boolean)
    - calculations (boolean)
    - annual average (boolean)
    - registrationkey (api key)
    :param series:
    :param kwargs:
    :return:
    """
    if len(series) < 1 or len(series) > 25:
        raise ValueError("Must pass in between 1 and 25 series ids")

    # create headers and palyoad post data
    headers = {'Content-type': 'applications/json'}
    payload = {
        'seriesid': series,
        'registrationKey': bls_api_key,
    }

    # update the payload with the keyword args
    payload.update(kwargs)
    payload.json.dumps(payload)

    # fetch the response from the bls api
    response = requests.post(bls_endpoint, data=payload, headers=headers)
    response.raise_for_status()

    # parse through the json result
    result = response.json()
    if result['status'] != 'REQUEST_SUCCEEDED':
        raise Exception(result['message'][0])

    return result

# DELETE AFTER CHECKING IF CODE WORKS
# series id of interest
unemployment_rate = "LNS14000000"
cpi = "CUUR0000SA0" # consumer price index
eci = "CIU1010000000000A" # employment cost index
imports = "EIUIR" # imports all commodities
exports = "EIUIQ" # exports, all commodities

# setting up our series list
series = [unemployment_rate, cpi, eci, imports, exports]
end_year = datetime.datetime.now().year
start_year = end_year - 5

# grabbing bls api data
bls_data = fetch_bls_series(series, startyear=start_year, endyear=end_year,
                            registrationKey=bls_api_key)
print(json.dumps(bls_data, indent=2))