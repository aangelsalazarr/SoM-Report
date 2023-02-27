import json
import pandas as pd
import os
from matplotlib import rc
import seaborn as sns
from datetime import date
from black_box.eia_data_processor import *
from dateutil.relativedelta import relativedelta
import null
import itertools
import numpy as np

# setting up current date variables
today = date.today()
current_date = today.strftime('%m_%d_y')

# here we can changes years variable to define how further back we want to go
start_date = today - relativedelta(years=5)

# setting up our api key
api_key = os.environ.get('eia_key')

# this will be the base url that we use related to AEO
base_url = 'https://api.eia.gov/v2/aeo/2022/data/'

# these are the params for aeo that we would like to grab
aeo_params = {
    "frequency": "annual",
    "data": [
        "value"
    ],
    "facets": {
        "tableId": [
            13,  # natural gas supply, disposition, and prices
            14,  # oil and gas supply
            17,  # energy related carbon dioxide emissions by sector and source
            22,  # energy related carbon dioxide emissions by end use
            3,   # energy prices by sector and source
            34,  # industrial sector macro economic conditions
            35,  # refining industry energy consumption
            38,  # bulk chemical industry energy consumption
            40,  # cement and lime industry energy consumption
            41,  # iron and steel industry energy consumption
            42,  # aluminum industry energy consumption
            58,  # freight transportation energy use
            6,   # industrial sector key indicators and consumption
            70,  # components of selected petroleum product prices
            71,  # lower 58 crude oil prod and wellhead prices by supply/region
            72,  # lower 48 nat gas prod adn supply prices by supply region
            76,  # nat gas imports and exports
            77,  # nat gas consumption by end user sector and census division
            78,  # nat gas delivered prices by end use sector and census
            90,  # primary nat gas flows entering nat gas market module region
        ],
        "scenario": [
            "aeo2021ref",  # AEO2021 reference case
            "awa10yr",  # AWA 10 year historical trend
            "awarcc",  # awa -  rate change: cooler
            "awarcw",  # awa - rate change: warmer
            "extendcred_i",  # alternative policies - extended credit
            "highmacro",  # high economic growth
            "highogs",  # high oil and gas supply
            "highprice",  # high oil price
            "hirencst",  # high renewables cost
            "hmc35",  # alternative policies $35 farbon fee high growth
            "lmc35",  # alternative policies $35 carbon fee low growth
            "logs_noarb",  # battery storage - capacity only low oil/gas supply
            "logs_norm",  # battery storage - energy only low oil/gas supply
            "lorencst",  # low renewables cost
            "lowmacro",  # low economic growth
            "lowogs",  # low oil and gas supply
            "lowprice",  # low oil price
            "lrc_noarb",  # battery storage - capacity only low renewables cost
            "lrc_norm",  # batter storage - energy only low renewable costs
            "ng_iif_final",  # no interstate pipeline builds
            "ref2022",  # reference case
            "ref_noarb",  # battery storage capacity only referece
            "ref_norm",  # battery storage energy only reference
            "refc15",  # alt policies $15 carbon fee reference
            "refc25",  # alt policies #25 carbon fee reference
            "refc35",  # alt polivies $35 carbon fee reference
            "sunsetcred_i"  # alt policies - sunset credit
        ]
    },
    "start": null,
    "end": null,
    "sort": [
        {
            "column": "period",
            "direction": "desc"
        }
    ],
    "offset": 0,
    "length": 5000
}


# allows us to add key, values to dictionaries
def add(self, key, value):
    self[key] = value


def create_params(permutations, facets):

    # this is a barebones params json object for eia data requests
    params = {
        "frequency": "monthly",
        "data": [
            "quantity"
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
        "length": 5000
    }

    # creating our main dataframe
    main_df = pd.DataFrame()

    """
    purpose of this function is to create a params framework for each perm
    so that we can store it in a list of permutated params
    this list will then be used to iterate through process of grabbing data
    from EIA with params with each permutation
    as we are iterating through grabbing data, we will store into 1 main data
    frame. this dataframe will then be outputted as an excel sheet so that 
    we can begin to deconstruct and analyze the data
    
    :param permutations: 
    :param json_obj: 
    :return: 
    """

    # add our facets to params json object
    for facet in facets:
        params['facets'].add(facet, '')

    for perm in permutations:

        # now we iterate through perms and create params json for each
        print('empty')

    print(params)

    return params



# df = params_2_data(json_obj=aeo_params, base_url=base_url, key=api_key)


# given n facet related objects, returns permutations
def find_permutations(lists):
    # Use itertools.product to find all possible combinations of one
    # element from each list
    perms = list(itertools.product(*lists))

    # Return the list of permutations
    return perms


# playing around lets goooo
def convert_facets(json_obj):
    # create urls list to store url segments
    url_segs = []

    # create list to store lists of facets
    facets = []

    # grabbing facets dictionary
    facet_dict = json_obj['facets']

    print('Facets dictionary: ')
    print(facet_dict, "\n")

    # iterate through dictionary
    for key, value in facet_dict.items():

        # store values in facets
        facets.append(list(value))

    print("Facets List: ")
    print(facets, "\n")

    # now we will find all possible permutations of our facets lists
    perms = find_permutations(facets)
    perms = np.array(perms)

    print("Permutations: ")
    print(perms, "\n")

    # converting each array in perms back into dictionary with key, value pairs


    # storing facet name and list of facet_items
    facet_id = list(facet_dict.keys())  # grabs first item in list
    facet_items = list(facet_dict.values())  # grabs first list in list

    # converting face_it to tuple to input into dictionary later
    facet_id_array = np.array(facet_id)

    # so we can view out facet ids and items
    print("tuple of facet types in our params: ", facet_id_array, "\n")
    print("list of what's in each facet: ", facet_items, "\n")
    print(f"There exist {len(perms)} permutations!", "\n")

    for item in facet_items:
        # storing item as url segment
        url_seg = "&" + f"facets[{facet_id}][]=" + str(item)

        # adding url segment to url segment list
        url_segs.append(url_seg)

    # concatenate urls segs into facets_url
    facets_url = "".join(url_segs)

    return facets_url, perms, facets



x = convert_facets(json_obj=aeo_params)
create_params(permutations=x.perms, facets=x.facets)

