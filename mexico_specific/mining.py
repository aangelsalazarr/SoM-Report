from black_box.inegi_data_processor import grab_inegi_data
from black_box.three_by_three_grapher import inegi_visualizer
from black_box.pdfConverter import save_multi_image
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date
import os

# purpose is to create current date and current year function
today = date.today()
currentDate = today.strftime('%m_%d_%y')

simbolico = os.environ.get('inegiKey')

# mining ids
mining = {
    '5300000005': 'Economic unites, sector 21, mining',
    '5300000025': 'Total renumeration, sector 21, mining',
    '5300000035': 'Total gross production, sector 21, mining',
    '5300000045': 'Total stock of fixed assets, sector 21, mining',
    '5300000095': 'Recenue from provision of goods and services, sector 21, '
                  'mining',
    '5300000105': 'Total expenditures for consumption of goods and services, '
                  'sector 21, mining',
    '6207046219': 'Volume of mining production, Gold, by state',
    '6207046220': 'Volume of mining production, Zinc, by state',
    '6207046221': 'Volume of mining production, Copper, by state',
    '6207046224': 'Volume of mining production, Silver by state',
    '6207046223': 'Volume of mining production, Lead, by state',
    '6207046230': 'Volume of mining production, Iron Pellets, by state',
    '6207046231': 'Volume of mining production, Iron Extraction by state',
    '6207046225': 'Volume of mining production, Sulfur, by state',
    '6207046226': 'Volume of mining production, Baryte, by state',
    '6207046227': 'Volume of mining production, Fluorite, by state',
    '6207046222': 'Volume of mining production, Coke, by state'
}

# geo ids
geos = {'0700':'nacional',
        '07000001': 'not sure what this is'}

# data bridge, note mining is always going to be BISE
bridges = {'BIE':'Bank for Economic Information',
           'BISE':'Bank of Indicators'}

# creating a list of keys
min_keys = list(mining.keys())
min_prods = min_keys[6:15]
geo_keys = list(geos.keys())
bridge_keys = list(bridges.keys())


# iterate
# storing grabbing of data
df_gold = grab_inegi_data(indicator=min_keys[6], geo=geo_keys[1],
                     bridge=bridge_keys[1])

df_zinc = grab_inegi_data(indicator=min_keys[7], geo=geo_keys[1],
                     bridge=bridge_keys[1])

df_cu = grab_inegi_data(indicator=min_keys[8], geo=geo_keys[1],
                     bridge=bridge_keys[1])

df_coke = grab_inegi_data(indicator=min_keys[9], geo=geo_keys[1],
                     bridge=bridge_keys[1])

df_silver = grab_inegi_data(indicator=min_keys[10], geo=geo_keys[1],
                     bridge=bridge_keys[1])

df_lead = grab_inegi_data(indicator=min_keys[11], geo=geo_keys[1],
                     bridge=bridge_keys[1])

df_sulfur = grab_inegi_data(indicator=min_keys[12], geo=geo_keys[1],
                     bridge=bridge_keys[1])

df_baryte = grab_inegi_data(indicator=min_keys[13], geo=geo_keys[1],
                     bridge=bridge_keys[1])

df_flourite = grab_inegi_data(indicator=min_keys[14], geo=geo_keys[1],
                     bridge=bridge_keys[1])

df = [df_gold, df_zinc, df_cu, df_coke, df_silver, df_lead, df_sulfur,
      df_baryte, df_flourite]


# putting our 9 mining resources in 3x3 graph
inegi_visualizer(list=df, list2=min_prods, x_axis='TIME_PERIOD',
                 y_axis='OBS_VALUE', fig_title='Mexico, Mining Production')


filename = 'data_visuals\mexico_mining_production'
save_multi_image(filename + currentDate + '.pdf')

