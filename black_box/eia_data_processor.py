import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns

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
def params_2_data(json_obj, base_url, key, facets_index):
    base = base_url
    freq = '&frequency=' + str(json_obj['frequency'])
    data_in = '&data[0]=' + str(json_obj['data'][0])
    facet = '&facets[product][]=' + str(
        json_obj['facets']['product'][facets_index])
    start = '&start=' + str(json_obj['start'])
    # end = json_obj['end']

    # concatenating all url segments
    url = str(base) + '?api_key=' + str(key) + str(freq) + str(data_in) + \
          str(facet) + str(start)

    # GET request to eia api
    r = requests.get(url=url)
    data = r.json()
    entries = data['response']['data']
    df = pd.DataFrame(data=entries)  # converting to pandas df
    df.reset_index(drop=True)  # resetting index as to remove date index
    # df['period'] = pd.to_datetime(df['period'])  # converting period col to
    # date

    print('Data Successfully Collected!')
    return df


def eia_visualizer_by_prod(df, products):

    for obj in products:
        plt.figure()
        x = sns.lineplot(data=df[df['product'] == obj],
                         x='period',
                         y='value',
                         color='maroon').set(title=obj)

        # rotate our xticks 90 degrees
        plt.xticks(rotation=90)



def combine_dfs(dfs):
    combined_df = pd.concat(dfs, axis=0, ignore_index=True)

    return combined_df


def save_multi_image(filename):
    pp = PdfPages(filename)
    fig_nums = plt.get_fignums()
    figs = [plt.figure(n) for n in fig_nums]
    for fig in figs:
        fig.savefig(pp, format='pdf')
    pp.close()
