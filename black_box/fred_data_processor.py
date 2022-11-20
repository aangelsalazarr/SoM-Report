import fredapi as fa
from datetime import date
import os
import pandas as pd

# time related stuff
today = date.today()
currentDate = today.strftime('%m_%d_%y')

# setting up any api keys that we may need
fredKey = os.environ.get('FREDKEY')


# creating function
def grab_fred_data(apikey, seriesid):
    # grabbing series id data
    fred = fa.Fred(api_key=apikey)
    data = fred.get_series(seriesid)
    df = pd.DataFrame(data=data)
    df.reset_index(inplace=True)
    df = df.rename(columns={'index': 'Date'})
