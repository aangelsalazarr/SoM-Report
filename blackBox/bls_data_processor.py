import pandas as pd
import requests
import json
import os

# api key and end point
bls_api_key = os.environ.get('blsAPI')
bls_endpoint = "https://api.bls.gov/publicAPI/v2/timeseries/data/"


# out general defn
def fetch_bls_series(series, **kwargs):
    """
    pass in a list of BLS timeseries to fetch data and return the series
    in JSON format. Args can also be provided as kwargs:
    - start-year
    - end-year
    - catalog (boolean)
    - calculations (boolean)
    - annual average (boolean)
    - registration (api key)
    """
    if len(series) < 1 or len(series) > 25:
        raise ValueError("Must pass in between 1 and 25 series ids")

    # create headers and payload post data
    headers = {'Content-type': 'application/json'}
    payload = {
        'seriesid': series,
        'registrationKey': bls_api_key,
    }

    # update the payload with the keyword args
    payload.update(kwargs)
    payload = json.dumps(payload)

    # fetch the response from the bls api
    response = requests.post(bls_endpoint, data=payload, headers=headers)
    response.raise_for_status()

    # parse through the json result
    result = response.json()
    if result['status'] != 'REQUEST_SUCCEEDED':
        raise Exception(result['message'][0])

    # grabbing list of series
    blsDataList = result['Results']['series']

    # create df to add incoming dfs
    df = pd.DataFrame(columns=['seriesID'])

    # purpose is to loop through each item and add to our df
    for item in blsDataList:
        df = pd.concat([df, pd.DataFrame(data=item['data'])])

        if df['seriesID'].isnull:
            df['seriesID'].fillna(item['seriesID'], inplace=True)
        else:
            continue

    df = df.drop(['latest', 'footnotes'], axis=1)
    df['Date'] = df['periodName'] + '-' + df['year']
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.reset_index(drop=True)

    # change value type to float
    df['value'] = df['value'].astype(float)

    return df
