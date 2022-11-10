import requests
import json
import os
import pandas as pd

# want to load into our environment our api key
simbolico = os.environ.get('inegiKey')

# dictionary storing possible request types
indicators = {'510108':'producto interno bruto (total nacional)',
              '497676':'actividad turistica, base 2013, indices de vol fisico',
              '1002000001':'poblacion total'}
geos = {'0700':'nacional'}
bridges = {'BIE':'Bank for Economic Information'}

# calling api
base = 'https://en.www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/'
id_ind = list(indicators.keys())[0] + '/'  # id indicator
lang = 'en' + '/'  # or 'es' for spanish language
geo = list(geos.keys())[0] + '/'  # geographic area
recents = 'false/'  # or 'false/' for if you want historical data?
data_bridge = list(bridges.keys())[0] + '/'  # not sure what this is tbh
v = '2.0/'  # not sure what else you could put here for version
token_n_type = simbolico + '?type=json'  # api key

# url segments concatenated
url = base + id_ind + lang + geo + recents + data_bridge + v + token_n_type
print(url)

# response var
response = requests.get(url=url)




