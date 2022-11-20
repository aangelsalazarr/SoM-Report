import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# params to use when testing code
tests = {'key_1':'CompactData/IFS/M.GB.PMP_IX',
         'data_path_1':'./tests/UK_import_price_index.csv',
         'fig_title_1':'U.K. Import Prices, (Index, 2010=100)'}


def grab_imf_data_(key, data_path):

    url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'
    params = key  # adjust codes here

    # Navigate to series in API-returned JSON data
    data = (requests.get(f'{url}{params}').json()['CompactData']['DataSet']['Series'])

    baseyr = data['@BASE_YEAR']  # Save the base year

    # Create pandas dataframe from the observations
    data_list = [[obs.get('@TIME_PERIOD'), obs.get('@OBS_VALUE')]
                 for obs in data['Obs']]

    df = pd.DataFrame(data_list, columns=['date', 'value'])
    df['date'] = pd.to_datetime(df['date'])
    df['value'] = df['value'].astype(float)

    df = df.assign(day_pct_change=df['value'].pct_change())

    # Save cleaned dataframe as a csv file
    df.to_csv(data_path, header=True, index=False)

    return df


# running a test run
df = grab_imf_data_(key=tests['key_1'], data_path=tests['data_path_1'])

print(df)

# plotting figures by creating axes object
# using subplots() function
fig, ax = plt.subplots()
plt.title(tests['fig_title_1'])

# using the twinx() for creating another
# axes object for secondary y-Axis
ax2 = plt.twinx()
sns.lineplot(data=df, x='date', y='day_pct_change', ax=ax,
             color='pink')
sns.lineplot(data=df, x='date', y='value', ax=ax2)



plt.show()




