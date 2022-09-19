import datetime
import requests  # pip install requests
import os
from datetime import date

'''
URL: https://www.gsam.com/content/dam/gsam/pdfs/common/en/public/articles/global-market-monitor/2022/market_monitor_091622.pdf?sa=n
https://www.gsam.com/content/dam/gsam/pdfs/common/en/public/articles/global-market-monitor/2022/market_monitor_091622.pdf?sa=n
urlSegment1 = https://www.gsam.com/content/dam/gsam/pdfs/common/en/public/articles/global-market-monitor/
urlSegment2 = 2022/market_monitor_091622.pdf?sa=n

'''

'''
We would like to break the url into segments so that we can address any char
changes in the url in the near future. the two things that we can def anticipate
include the year and the date within the url that are subject to change
'''
# grabbing today's date
today = date.today()

# creating today's date formatted as %m%d%y
todayReformat = today.strftime("%m%d%y")

# creating current year
currentYear = today.strftime('%Y')

# breaking url into segments to address variable url snippets
urlSeg1 = 'https://www.gsam.com/content/dam/gsam/pdfs/common/en/public/articles/global-market-monitor/'
urlSeg2 = str(currentYear)
urlSeg3 = '/market_monitor_'
urlSeg4 = str(todayReformat)
urlSeg5 = '.pdf?sa=n'

# recombining our url now that we acounted for changes in url in T+1
gsMMUrl = urlSeg1 + urlSeg2 + urlSeg3 + '09162022' + urlSeg5

# creating where to store pdf
output_dir = '.\gsMarketMonitor'

response = requests.get(gsMMUrl)

print(response)
print(gsMMUrl)

# process to grab goldman sachs market monitor
if response.status_code == 200:
    x = os.path.basename(gsMMUrl)
    x = x[:-5]
    file_path = os.path.join(output_dir, x)
    # file.write(f'{datetime.datetime.now()}: A pdf successfully downloaded.
    # \n')
    with open(file_path, 'wb') as f:
        f.write(response.content)
    print('it worked!')
else:
    # file.write(f'{datetime.datetime.now()}: the script ran without pdf '
               # f'download. \n')
    print(f"Response: {response}")
    print("No PDF found.")

    # not wokring



