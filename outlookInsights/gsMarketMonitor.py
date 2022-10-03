from fpdf import FPDF
from bs4 import BeautifulSoup
import requests
from datetime import date

# setting up our year and date to match with the general url framework
today = date.today()
currentDate = today.strftime("%m%d%y")
currentYear = today.strftime('%Y')

# breaking our very long url into segments to take into account variable aspects
url1 = "https://www.gsam.com/content/gsam/us/en/individual/market-insights/"
url2 = "market-strategy/global-market-monitor/"
url3 = str(currentYear)
url4 = "/market_monitor_"
url5 = str(currentDate)
url6 = ".html"

# combining all of our urls into one
urlSegments = [url1, url2, url3, url4, url5, url6]

# concatenating our list of urls to create the full url up to date
urlFull = ''.join(urlSegments)

# extracting html from the website page
html = requests.get(urlFull)
soup = BeautifulSoup(html.content, "html.parser")

# let's view our html code now to see the break up
print(soup.prettify())
print(urlFull)




