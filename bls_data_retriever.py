# purpose is to grab data form bls public api
# this pyscript will be used ot create functions

import requests
import json
import os


class bls_data:

    def __init__(self, reg_key, series_id, start_year, end_year):

        # set the file name variable and create the params for the api request
        #self.out_file_nm = out_file_nm

        headers = {'Content-type' : 'application/json'}
        params = json.dumps({'seriesid':series_id, 'startyear':start_year,
                             'endyear':end_year, 'calculations':True,
                             'registrationkey':reg_key})

        # retrieve data in json format
        json_data = self.get_data(headers, params)

    def get_data(self, headers, params):

        # post the data request to the bls api, return resulting in a json
        post = requests.post('https://api.bls.gov/publicAPI/v2/timeseries'
                             '/data/', data = params, headers = headers)
        json_data = json.loads(post.text)

        return json_data


