'''
Purpose of this script is to grab and process the CIO daily updates report from
UBS Wealth Management USA, Investment research, investment insights from the
Chief Investment Office
'''
from datetime import date
from urllib.request import urlopen

import pdfkit
from bs4 import BeautifulSoup
import requests

# setting up our Year and current date to insert in url 4 and 6
today = date.today()
currentDate = today.strftime("%d%m%Y")
currentYear = today.year

# breaking our very long url into segments that will fit within 80 char width
url1 = 'https://www.ubs.com/us/en/wealth-management/insights/'
url2 = 'investment-research/insights-display-adp/global/en/wealth-management/'
url3 = 'insights/chief-investment-office/house-view/daily/'
url4 = str(currentYear)
url5 = '/latest-'
url6 = str(currentDate)
url7 = '.html?caasID=CAAS-ActivityStream'

# combining all urls in  a list
urlSegments = [url1, url2, url3, url4, url5, url6, url7]

# concatenating list segments into one complete url
urlFull = ''.join(urlSegments)

# extracting html from the website page
html = requests.get(urlFull)
soup = BeautifulSoup(html.content, "html.parser")

# extracting text from the url
totdContent = soup.find_all('p')
totdContent = totdContent[4:-9]

# opening file path
fp = open(r'File_Path', 'w')

'''
# open file in write mode
with open(r'./ubsDailyUpdate')
for item in totdContent:
    print(item)
'''

'''
# combining all grabbed content into a long string
fullStr = ''

for item in totdContent:
    fullStr.join(str(item))

pdfkit.from_string(fullStr, "ThoughtoftheDay_" + str(currentDate) + ".pdf",
                       verbose=True)

'''
