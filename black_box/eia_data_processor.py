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
api_key = 'NrKy4od177sFNGfaZ9qOe17kj6f9iFk78aAKdSe8'


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


# purpose is to input an eia params json object and return data
def params_2_data(json_obj, base_url, key):

    base = base_url
    freq = '&frequency=' + str(json_obj['frequency'])
    data_in = '&data[0]=' + str(json_obj['data'][0])
    sort = "&sort[0][column]=period"
    direction = "&sort[0][direction]=desc"
    offset = '&offset=0'
    length = "&length=5000"

    if len(json_obj['facets']) > 0:
        facet = convert_facets(json_obj)
        # start = '&start=' + str(json_obj['start'])
        # end = json_obj['end']

        # concatenating all url segments
        url = str(base) + '?api_key=' + str(key) + str(freq) + str(data_in) + \
              str(facet) + str(sort) + str(direction) + str(
            offset) + str(length)

        print(url)

    else:

        # want to let user know that facets is empty in params
        print('Facets Object Length is =< 0!')

        start = '&start=' + str(json_obj['start'])

        # concatenating all url segments
        url = str(base) + '?api_key=' + str(key) + str(freq) + str(data_in) + \
              str(start) + str(sort) + str(direction) + str(offset) + str(
            length)

        print(url)

    # GET request to eia api
    r = requests.get(url=url)
    data = r.json()

    entries = data['response']['data']
    df = pd.DataFrame(data=entries)  # converting to pandas df
    df.reset_index(drop=True)  # resetting index as to remove date index
    # df['period'] = pd.to_datetime(df['period'])  # converting period col to
    # date
    # df['pct_change'] = df['value'].pct_change()
    # df['pct_change'] = df['pct_change'] * 100
    # df['period'] = df['period'].dt.strftime('%m-%Y')

    print('Data Successfully Collected!')
    print(df.describe())
    print(df.dtypes)
    print(df)

    return df


def facets_processor(facet_type, obj, facets_index):
    '''
    The purpose of this function is to process facet by whichever type of
    facet exists in the params we are processing

    Here are the type of facets that are possible:
    - product
    - series
    - duoarea
    - process
    - tableId
    '''

    # want to begin with a counter
    counter = 0

    # grabbing our dictionary from facets
    facet_dict = obj['facets']

    while counter <= len(facet_dict):

        # in essence, while counter is  less than length of facet
        # types, apply this functio

        for facet in facet_dict:

            if facet == "product":

                f = '&facets[product][]=' + str(
                    obj['facets']['product'][facets_index])

                print('')

            elif facet == "series":

                f = '&facets[]'

                print('')

            elif facet == 'tableId':
                f = '&facets[tableId][]' + str(
                    obj['facets']['tableId'][facets_index])

                print('')

            elif facet == "process":

                print('')

            else:
                '''
                this is for situation in which facet type is duoarea
                '''

                print('')

    facet = '&facets[' + str(facet_type) + '][]=' + str(
        obj['facets'][str(facet_type)][facets_index])

    return facet


# playing around lets goooo
def convert_facets(json_obj):
    # create urls list to store url segments
    url_segs = []

    # grabbing facets dictionary
    facet_dict = json_obj['facets']

    # storing facet name and list of facet_items
    facet_id = list(facet_dict.keys())[0]  # grabs first item in list
    facet_items = list(facet_dict.values())[0]  # grabs first list in list

    for item in facet_items:
        # storing item as url segment
        url_seg = "&" + f"facets[{facet_id}][]=" + str(item)

        # adding url segment to url segment list
        url_segs.append(url_seg)

    # concatenate urls segs into facets_url
    facets_url = "".join(url_segs)

    return facets_url


def eia_visualizer_by_prod(df, products):
    for obj in products:
        plt.figure()
        x = sns.lineplot(data=df[df['product'] == obj],
                         x='period',
                         y='value',
                         color='maroon').set(title=obj)


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
