import datetime
import requests  # pip install requests
import os
from datetime import date

'''
CMO Outlook--
url: https://openknowledge.worldbank.org/bitstream/handle/10986/37223/CMO-April-2022.pdf
urlSegment1= 'https://openknowledge.worldbank.org/bitstream/handle/10986/37223/CMO-'
urlSegment2= 'April-2022'
urlSegment3= '.pdf'

CMO price update monthly--
url: https://thedocs.worldbank.org/en/doc/5d903e848db1d1b83e0ec8f744e55570-0350012021/related/CMO-Pink-Sheet-September-2022.pdf
segment1: https://thedocs.worldbank.org/en/doc/5d903e848db1d1b83e0ec8f744e55570-0350012021/related/CMO-Pink-Sheet-
segment2: September-2022
segment3: .pdf
'''

# path for the cmo & commodity prices pinksgeet
output_dir1 = '.\wbCMO'
output_dir2 = '.\wbCMO'

# grabbing today's date to be used in our url_date variable
today = date.today()

# need to convert our date to fit format used in url
today_reformat = today.strftime("%B-%Y")

urlSeg1CMO = 'https://openknowledge.worldbank.org/bitstream/handle/10986' \
             '/37223/CMO-'
urlSeg2CMO = '.pdf'

# segments for pink sheet
urlSeg1PS ='https://thedocs.worldbank.org/en/doc/5d903e848db1d1b83e0ec8f744e55570-0350012021/related/CMO-Pink-Sheet-'
urlSeg2PS = '.pdf'

wbCMOUrl = urlSeg1CMO + today_reformat + urlSeg2CMO
wbCommodityPS = urlSeg1PS + today_reformat + urlSeg2PS

response1 = requests.get(wbCMOUrl)
response2 = requests.get(wbCommodityPS)

# process to grab cmo
if response1.status_code == 200:
    file_path = os.path.join(output_dir1, str(today_reformat) + '_' +
    os.path.basename(wbCMOUrl))
    # file.write(f'{datetime.datetime.now()}: A pdf successfully downloaded.
    # \n')
    with open(file_path, 'wb') as f:
        f.write(response1.content)
else:
    # file.write(f'{datetime.datetime.now()}: the script ran without pdf '
               # f'download. \n')
    print(f"Response: {response1}")
    print("No PDF found.")

# process to grab commodities pinksheet
if response2.status_code == 200:
    file_path = os.path.join(output_dir2, os.path.basename(wbCommodityPS))
    # file.write(f'{datetime.datetime.now()}: A pdf successfully downloaded.
    # \n')
    with open(file_path, 'wb') as f:
        f.write(response2.content)
else:
    # file.write(f'{datetime.datetime.now()}: the script ran without pdf '
               # f'download. \n')
    print(f"Response: {response2}")
    print("No PDF found.")

