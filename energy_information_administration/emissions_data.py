from eia_data_processor import grab_eia_data, is_float
from black_box.pdfConverter import save_multi_image
import os
from datetime import date
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
from matplotlib import rc
import seaborn as sns


# some params related to the framework of pdf output that we will need
rc('mathtext', default='regular')
plt.rcParams["figure.autolayout"] = True

# grabbing our api key
api_key = os.environ.get('eiaAPI')

# setting up some date variables to use
today = date.today()
currentDate = today.strftime('%m_%d_%y')
startDate = today - relativedelta(years=5)
eiaStartDate = startDate.strftime('%Y')



# base url
baseUrl = 'https://api.eia.gov/v2/co2-emissions/co2-emissions-aggregates/data/'
baseUrl = baseUrl + '?api_key=' + str(api_key)

# we will want to add some inputs to our complete url
urlData = '&data[0]=value'
urlFreq = '&frequency=annual'
urlStart = '&start=' + str(eiaStartDate)

# concatenate to get main url
mainUrl = baseUrl + urlData + urlFreq + urlStart

# storing our get request as a df variable
df = grab_eia_data(url=mainUrl)

# getting rid of any non numeric values in the value col
df = df[df['value'].apply(lambda x: is_float(x))]

# converting df to csv data file
## df.to_csv('.\data_files\emissions_data.csv', index=False)

# bifurcating into two types of dfs w and w/o total emissions data
df_non_total = df[(df['sectorId'] != 'TT') & (df['fuelId'] != 'TO') & (df[
    'stateId'] != 'US')]
df_total = df[(df['sectorId'] == 'TT') & (df['fuelId'] == 'TO') & (df[
    'stateId'] == 'US')]

# visualizing data
fig1 = plt.figure()
co2_by_sector = sns.barplot(data=df_non_total, x='period', y='value',
                             hue='sector-name', ci=None)
co2_by_sector.set(xlabel=None, ylabel=df['value-units'][0])
#place legend outside center right border of plot
plt.legend(bbox_to_anchor=(1.02, 0.55), loc='upper left', borderaxespad=0)


fig2 = plt.figure()
co2_by_fuel = sns.barplot(data=df_non_total, x='period', y='value',
                           hue='fuel-name', ci=None)
co2_by_fuel.set(xlabel=None, ylabel=df['value-units'][0])
#place legend outside center right border of plot
plt.legend(bbox_to_anchor=(1.02, 0.55), loc='upper left', borderaxespad=0)


# plotting co2 emissions of top 10 polluters
top_ten = ['TX', 'CA', 'FL', 'PA', 'IL', 'OH', 'LA', 'IN', 'NY', 'MI']
df_top_ten = df_non_total[df_non_total['stateId'].isin(top_ten)]

fig3 = plt.figure()
co2_by_state = sns.lineplot(data=df_top_ten,
                           x='period', y='value',
                           hue='state-name', ci=None)
co2_by_state.set(xlabel=None, ylabel=df['value-units'][0])
#place legend outside center right border of plot
plt.legend(bbox_to_anchor=(1.02, 0.55), loc='upper left', borderaxespad=0)


# saving to pdf file
filename = '.\data_visuals\co2_emissions_visuals_'
save_multi_image(filename + currentDate + '.pdf')



