import requests
import json
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# want to load into our environment our api key
simbolico = os.environ.get('inegiKey')

# dictionary storing possible request types
indicators = {'510108':'producto interno bruto (total nacional)',
              '497676':'actividad turistica, base 2013, indices de vol fisico',
              '1002000001':'poblacion total'}
pop_migration = {
    '6200205255': 'Immigration Population, 5 yrs and over',
    '6200205252': '% international migran pop. headed to other country',
    '6200205262': 'International migration net balance of 5 yrs and over',
    '6200205264': '% international migrant with no destination',
    '6200240349': '% international migration to USA',
    '6200240327': '% of international migration to rest of world',
    '6200240404': '% international migrant pop. due to public '
                  'insecurity/violence',
    '6200240415': '% of international migrant pop. to unspecified countries',
    '6207129645': '% migrant pop. of 5 yrs and over according to: education',
    '6207129646': '% migrant pop. of 5 yrs or over according to: criminal '
                  'insecurity or violence'
}

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
    '6207046222': 'Volume of mining production, Coke, by state',
    '6207046224': 'Volume of mining production, Silver by state',
    '6207046223': 'Volume of mining production, Lead, by state',
    '6207046225': 'Volume of mining production, Sulfur, by state',
    '6207046226': 'Volume of mining production, Baryte, by state',
    '6207046227': 'Volume of mining production, Fluorite, by state',
    '6207046230': 'Volume of mining production, Iron Pellets, by state',
    '6207046231': 'Volume of mining production, Iron Extraction by state',
}

geos = {'0700':'nacional',
        '07000001': 'not sure what this is'}

bridges = {'BIE':'Bank for Economic Information',
           'BISE':'Bank of Indicators'}


def grab_inegi_data(indicator, geo, bridge):
    # calling api
    base = 'https://en.www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/'
    ind = indicator + '/'  # id indicator, list(mining.keys())[6]
    lang = 'en' + '/'  # or 'es' for spanish language
    geo_id = geo + '/'  # geographic area, list(geos.keys())[1]
    recents = 'false/'  # or 'false/' for if you want historical data?
    data_bridge = bridge + '/'  # list(bridges.keys())[1]
    v = '2.0/'  # not sure what else you could put here for version lol
    token = simbolico + '?type=json'  # api key
    # url segments concatenated
    url = base + ind + lang + geo_id + recents + data_bridge + v + token

    # response var
    response = requests.get(url=url)
    data = response.json()
    entries = data['Series'][0]['OBSERVATIONS']
    df = pd.DataFrame(data=entries)
    df['TIME_PERIOD'] = pd.to_datetime(df['TIME_PERIOD'])
    df['OBS_VALUE'] = df['OBS_VALUE'].astype(float)

    return df






