from fpdf import FPDF
from bs4 import BeautifulSoup
import requests
from datetime import date
import re
import pdfkit

# setting up our year and date to match with the general url framework
today = date.today()
currentDate = today.strftime("%m%d%y")
currentYear = today.strftime('%Y')

# breaking our very long url into segments to take into account variable aspects
url1 = "https://www.gsam.com/content/gsam/us/en/individual/market-insights/"
url2 = "market-strategy/global-market-monitor/"
url3 = str(currentYear)
url4 = "/market_monitor_"
url5 = "093022"  #str(currentDate)
url6 = ".html"

# combining all of our urls into one
urlSegments = [url1, url2, url3, url4, url5, url6]

# concatenating our list of urls to create the full url up to date
urlFull = ''.join(urlSegments)

# extracting html from the website page
html = requests.get(urlFull)
soup = BeautifulSoup(html.content, "html.parser")

# let's only pull html code from the main content we are looking for
results = soup.find(class_="contentArea gm-clear_both")

'''
Following, we are going to break down the website into different sections of 
code that reflects general themes of the market monitor, each section will be
denoted as x_i and a sub section as x_i_j where i = [0, 1, .., N], j = [a, b,..]

#### Section 1
x_0: Chart of the week general heading title
x_1: chart of the week theme title
x_2: chart itself which is a .png entity
x_3: summary title related to the graph
    x_3_a: graph summary
    
#### Section 2
x_4: "market summary" title 
x_5: container where market summaries are stored
    x_5_a: global equity title
        x_5_aa: global equity summary
    x_5_b: commodities title
        x_5_bb: commodities summary
    x_5_c: fixed income title 
        x_5_cc: fixed income summary
    x_5_d: fx title
        x_5_dd: fx summary
    
#### Section 3
x_6: "Economic Summary" title
x_7: contained where economic summaries are stored
    x_7_a: inflation title
        x_7_aa: inflation summary
    x_7_b: policy title
        x_7_bb: policy summary
    x_7_c: activity title
        x_7_cc: activity summary
    x_7_d: labor title
        x_7_dd: labor summary

#### Section 4
x_8: container that contained sytle performance
x_8
... [to be continued]
'''

# working on section 1 which contains the chart of the week
# "Chart of the Week" Title
cowTitle = results.find("h2", class_="title2 titleSpacing2 js-title")

# contains market monitor theme title
themeTitle = results.find("div", class_="titleSummaryLink")

# contains chart of the week
chart = results.find("div", class_="imageleftRight__img gm-showScroll_touch")

# contains chart description
chartDescription = results.find("div", class_="imageleftRightDesc bm-spacing")

# contains "market summary" title
marketSumTitle = results.find("h2", class_="title3 titleSpacing3 js-title")

# contains market summary section titles and descriptions
marketSumContent = results.find("div", class_="compCont")

# let's actually just try converting html to pdf lol
path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

#Point pdfkit configuration to wkhtmltopdf.exe
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

#Convert HTML file to PDF
pdfkit.from_url(urlFull, output_path='sample.pdf', configuration=config)






