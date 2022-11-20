import requests
import pandas as pd

# test dictionary
tests = {
    'wealth':'https://stats.oecd.org/SDMX-JSON/data/WEALTH/AUS+AUT+BEL+CAN+CHL'
           '+DNK+EST+FIN+FRA+DEU+GRC+HUN+IRL+ITA+JPN+KOR+LVA+LTU+LUX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+GBR+USA.T1C5+MNWI+T1C6+M2MR+T3AC2+T3AC1+T3AC3+T4C5+T4C4+PIH+PIH75+PIHR3+T6AC2+T6AC3+T6AC6+T6AC7+ST1+ST5+ST10+SB40.TP/all?startTime=2009&endTime=2019&dimensionAtObservation=allDimensions'
}


def grab_oecd_data(url):

    # let's create an empty df
    df = pd.DataFrame(columns=['time', 'value'])

    # le'ts grab our data
    r = requests.get(url=url)
    data = r.json()
    entries = data['dataSets'][0]['observations']

    # iterate through entries and grab 1 item of list
    for key, value in entries.item():


    return entries


x = grab_oecd_data(url=tests['wealth'])

print(x)