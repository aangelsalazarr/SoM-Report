import wbgapi as wb
import pandas as pd
from datetime import date
import seaborn as sns
import matplotlib.pyplot as plt
from black_box.pdfConverter import save_multi_image

# setting up time related variables
today = date.today()
current_year = today.strftime('%Y')
previous_year = str(int(current_year) - 1)

# series list
series = ['SP.POP.TOTL', 'EN.ATM.GHGT.KT.CE']

# this is the data frame we will be working with
df = wb.data.DataFrame(series=series, economy='ALL',
                         time=2019,
                           columns='series', labels=True).reset_index()


# converting our pop_df into a csv to store as a data file
df.to_csv('./data_files/wb_data_2019.csv', index=False)

# visualizing data
fig1 = plt.figure()
world_pop = sns.scatterplot(data=df,
                            x='EN.ATM.GHGT.KT.CE', y='SP.POP.TOTL',
                            hue='Country', legend=False)

filename_2019_data = './data_visuals/wb_data_2019.pdf'

save_multi_image(filename_2019_data)
