'''
Overall purpose of this script is to web scrap for the most up to date news
on the Today In Energy segment on the EIA website

*EIA = Energy Information Administration
'''

# useful package for webscraping
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

# useful for converting svg to png
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

# the url we will be opening, in this case the homepage of EIA - Today in Energy
tieUrl = 'https://www.eia.gov/todayinenergy/'

# purpose is to open the webpage
page = urlopen(tieUrl)

# extracting html from the website page
htmlBytes = page.read()
html = htmlBytes.decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# extracting titles in webpage
titleIndex = html.find("<title>")
startIndex = titleIndex + len("<title>")
endIndex = html.find("</title>")
title = html[startIndex:endIndex]

# extracting all images and texts
images = soup.findAll('img')
texts = soup.get_text()

# converting the most up to date image to png from svg
# in essence, from any array, picture associated with most up to date article
# is the second item in the array returns from var images
drawing = svg2rlg('input/' + images[1]['src'])
renderPM.drawToFile(drawing, 'output/drawing.png', fmt='PNG')

print(texts)
print(images)
print(images[1]['src'])