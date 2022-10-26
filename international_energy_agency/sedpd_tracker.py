import pandas as pd
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
'''
purpose is to parse through IEA report on clean energy demonstration
project database and present everything in a visual manner
- country
- sector
- technologies
- name
- status
- capacity

may do
1. capacity by country and split said visual data by
    - sector
    - technology
    status
'''
# splitting our url to make it shorter
url1 = "https://www.iea.org/data-and-statistics/data-tools/"
url2 = "clean-energy-demonstration-projects-database"

# combining our segmented urls to become one big one
fullUrl = url1 + url2

# now we want to grab the datatable from the url
page = requests.get(fullUrl)

soup = BeautifulSoup(page.content, 'html.parser')
soup2 = BeautifulSoup(str(soup), 'lxml')

# now we want to look for our table
tables = soup.find_all("table")

# converting to df
# data_frame = pd.read_html(str(table))[0]

print(tables)
