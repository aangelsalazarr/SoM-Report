import pandas as pd
import matplotlib.pyplot as plt
from blackBox.bls_data_processor import fetch_bls_series
from blackBox.bls_data_processor_2 import bls_fetch_data
import seaborn as sns


# let's first pull unemployment data from BLS
ca_unem = ['LASST060000000000003', 'LASST060000000000004',
          'LASST060000000000005', 'LASST060000000000006',
          'LASST060000000000007', 'LASST060000000000008']

df = fetch_bls_series(series=ca_unem)

# output df as csv file
df.to_csv('.\data_files\data_ca_unemployment_bls.csv')

