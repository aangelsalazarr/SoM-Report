import wbgapi as wb
import pandas as pd
from datetime import date
import seaborn as sns
import matplotlib.pyplot as plt
from black_box.pdfConverter import save_multi_image
from black_box.wb_data_processor import *

# setting up time related variables
today = date.today()
current_year = today.strftime('%Y')
previous_year = str(int(current_year) - 1)

# creating a dictionary to store more info relates to series
series_dict = {'SP.POP.TOTL': 'population, total',
           'EN.ATM.GHGT.KT.CE': 'total greenhouse gas emissions, kt of c02 '
                                'equivalent',
           'EG.ELC.ACCS.ZS': 'access to electricity, % of population',
           'EG.USE.PCAP.KG.OE': 'energy use, kg of oil equivalent per capita',
               'BX.TRF.PWKR.CD.DT': 'personal remittances received, current '
                                    '$US',
               'EN.POP.SLUM.UR.ZS': 'pop. living in slums, % urban pop.'}

# let's grab our first df
df_2019 = grab_year_based_data(dictionary=series_dict, economy='ALL', time=2019)

# converting our pop_df into a csv to store as a data file
df_2019.to_csv('./data_files/wb_data_2019.csv', index=False)

