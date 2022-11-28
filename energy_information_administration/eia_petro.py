import null
from black_box.eia_data_processor import *
import os
import seaborn as sns
import matplotlib.pyplot as plt

# grabbing our eia api key
eia_key = os.environ.get('eiaKey')

# base urls related to petro prices
# Petro > prices > weekly retail gas and diesel prices
petro_gnd = 'https://api.eia.gov/v2/petroleum/pri/gnd/data/'
petro_spt = 'https://api.eia.gov/v2/petroleum/pri/spt/data/'
petro_fut = 'https://api.eia.gov/v2/petroleum/pri/fut/data/'

petro_weekly = {
    "frequency": "weekly",
    "data": [
        "value"
    ],
    "facets": {
        "product": [
            "EPD2D",  # facets_index = 0
            "EPMM",
            "EPMP",
            "EPMR"  # facets_index= 3
        ]
    },
    "start": "2015-01-01",
    "end": null,
    "sort": [
        {
            "column": "period",
            "direction": "desc"
        }
    ],
    "offset": 0,
    "length": 5000,
    "api-version": "2.0.4"
}

petro_spot = {
    "frequency": "weekly",
    "data": [
        "value"
    ],
    "facets": {
        "product": [
            "EPCBRENT",
            "EPCWTI",
            "EPD2DC",
            "EPD2F",
            "EPJK",
            "EPLLPA",
            "EPMRU"
        ]
    },
    "start": "2015-01-01",
    "end": null,
    "sort": [
        {
            "column": "period",
            "direction": "desc"
        }
    ],
    "offset": 0,
    "length": 5000,
    "api-version": "2.0.4"
}

# petro future
petro_futs = {
    "frequency": "weekly",
    "data": [
        "value"
    ],
    "facets": {
        "product": [
            "EPC0",
            "EPD2F",
            "EPLLPA",
            "EPMR",

        ]
    },
    "start": "2015-01-01",
    "end": null,
    "sort": [
        {
            "column": "period",
            "direction": "desc"
        }
    ],
    "offset": 0,
    "length": 5000,
    "api-version": "2.0.4"
}

# list of products available to filter by
products = [
    "EPD2D",  # facets_index = 0
    "EPMM",
    "EPMP",
    "EPMR",
    "EPCBRENT",
    "EPCWTI",
    "EPD2DC",
    "EPD2F",
    "EPJK",
    "EPLLPA",
    "EPMRU",
]

# dfs related to weekly retail gas and diesel prices
epd2d_df = params_2_data(json_obj=petro_weekly, base_url=petro_gnd,
                         key=eia_key, facets_index=0)
epmm_df = params_2_data(json_obj=petro_weekly, base_url=petro_gnd,
                        key=eia_key, facets_index=1)
epmp_df = params_2_data(json_obj=petro_weekly, base_url=petro_gnd,
                        key=eia_key, facets_index=2)
epmr_df = params_2_data(json_obj=petro_weekly, base_url=petro_gnd,
                        key=eia_key, facets_index=3)

# dfs relates to petro spot prices
epcbrent_df = params_2_data(json_obj=petro_spot, base_url=petro_spt,
                         key=eia_key, facets_index=0)
epcwti_df = params_2_data(json_obj=petro_spot, base_url=petro_spt,
                         key=eia_key, facets_index=1)
epd2dc_df = params_2_data(json_obj=petro_spot, base_url=petro_spt,
                         key=eia_key, facets_index=2)
epd2f_df = params_2_data(json_obj=petro_spot, base_url=petro_spt,
                         key=eia_key, facets_index=3)
epjk_df = params_2_data(json_obj=petro_spot, base_url=petro_spt,
                         key=eia_key, facets_index=4)
epllpa_df = params_2_data(json_obj=petro_spot, base_url=petro_spt,
                         key=eia_key, facets_index=5)
epmru_df = params_2_data(json_obj=petro_spot, base_url=petro_spt,
                         key=eia_key, facets_index=6)

# dfs related to petro futures prices
epc0_futs = params_2_data(json_obj=petro_futs, base_url=petro_fut,
                         key=eia_key, facets_index=0)
epd2f_futs = params_2_data(json_obj=petro_futs, base_url=petro_fut,
                         key=eia_key, facets_index=1)
epllpa_futs = params_2_data(json_obj=petro_futs, base_url=petro_fut,
                         key=eia_key, facets_index=2)
epmr_futs = params_2_data(json_obj=petro_futs, base_url=petro_fut,
                         key=eia_key, facets_index=3)

# storing our dfs into a list of dfs
dfs = [epd2d_df, epmm_df, epmp_df, epmr_df, epcbrent_df, epcwti_df, epd2dc_df,
       epd2f_df, epjk_df, epllpa_df, epmru_df, epc0_futs, epd2f_futs,
       epllpa_futs, epmr_futs]

# combining all dfs vertically
df_main = combine_dfs(dfs=dfs)

eia_visualizer_by_prod(df=df_main, products=products)

# let's now store our visualizations in a pdf format
filename = './data_visuals/eia_petro_visuals.pdf'
save_multi_image(filename)


'''
# converting df_main to csv
df_main.to_csv('./data_files/eia_petro_data.csv', index=False)
'''


