'''
Purpose of this script is to grab and process the CIO daily updates report from
UBS Wealth Management USA, Investment research, investment insights from the
Chief Investment Office
'''
from datetime import date
from urllib.request import urlopen

from fpdf import FPDF
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
mainText = soup.find(id="main")
textElements = mainText.find_all("p")


# purpose is to save all the text we are gathering into a pdf format
# save FPDF() class into a variable pdf
pdf = FPDF()

# add a page
pdf.add_page()

# setting style and font size that we want for the pdf
pdf.set_font("Helvetica", size=8)

# purpose is to iterate through texts and add to the pdf
for element in textElements:
    text = element.text.encode('latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(w=0, h=5, txt=text, align='L')

# now we want to output our pdf and ensure that the name is unique to the date
# when we grabbed the data or when the data was posted
pdf.output("CIO_Daily_Update_" + url6 + ".pdf")

