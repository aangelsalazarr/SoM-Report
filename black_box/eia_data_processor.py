import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

# setting up params
rc('mathtext', default='regular')
plt.rcParams['figure.autolayout'] = True

# storing our api key in var api_key
api_key = os.environ.get('eiaAPI')


# purpose is to take out any rows where value is not a number/float
def is_float(x):
    try:
        float(x)
    except ValueError:
        return False
    return True


# purpose is to grab data and transform it
def grab_eia_data(url):
    r = requests.get(url=url)  # store url request as variable r
    data = r.json()  # convert our request into json format
    entries = data['response']['data']  # only grabbing data aspect of return
    eia_df = pd.DataFrame(data=entries)  # converting our data into a pandas df
    eia_df.reset_index(drop=True)  # resetting df index
    eia_df['period'] = pd.to_datetime(eia_df['period'])  # convert period type

    return eia_df  # return our now transformed df


# purpose is to input a eia params json object and return data
def params_2_data(json_obj, base_url):
    base = base_url
    freq = json_obj['frequency']
    data_in = json_obj['data']
    facet = json_obj['facets']['product'][0]
    start = json_obj['start']
    end = json_obj['end']
    
    # concatenating all url segments
    url = base + freq + data_in + facet + start + end
    
    
    
    
    
    
    
    
    
    
    
    
    