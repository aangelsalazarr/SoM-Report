import datetime
import requests  # pip install requests
import os
from datetime import date

'''
In this file, we will be downloading the newest pdf from the merrill capital
markets outlook that is released essentially every week

this is the url for the most up to date Capital Market Outlook Webpage:
https://www.ml.com/capital-market-outlook/capital-market-outlook-sep-12-2022.recent.html

notice that url is the same and what changes is the date aspect of the url:
(sep-12-2022) -> (mmm-dd-yyyy)

this is the url for the most up to date cmo pdf that exists within the above
webpage: 
https://olui2.fs.ml.com/Publish/Content/application/pdf/GWMOL/CMO_9-12-22_Merrill.pdf

notice that the url is the same and what changes is the date aspect of the url:
(9-12-22) -> (m-dd-yy)

thus, let's split url into piece before date and piece after
url_segment_1 = 'https://olui2.fs.ml.com/Publish/Content/application/pdf/GWMOL/CMO_'
url_date = '9-12-22'
url_segment_2 = '_Merrill.pdf'

newest_cmo_url = url_segment_1 + url_date + url_segment_2

'''

# where the pdfs will be stored
output_dir = '.\merrill_pdfs'

# grabbing today's date to be used in our url_date variable
today = date.today()

# need to convert our date to fit format used in url
today_reformat = today.strftime("%#m-%#d-%y")


# combining our url segments
url_sgmnt_1 = 'https://olui2.fs.ml.com/Publish/Content/application/pdf/GWMOL/CMO_'
url_date = str(today_reformat)
url_sgmnt_2 = '_Merrill.pdf'

newest_cmo_url = url_sgmnt_1 + url_date + url_sgmnt_2

response = requests.get(newest_cmo_url)


'''
Purpose is to grab the pdf folder if the process is successful and then 
update a log stating at what time it was successful
'''
# creating path where the text file will exist
file = open(r'.\outlookLogger\merrillLogger.txt', 'a')

if response.status_code == 200:
    file_path = os.path.join(output_dir, os.path.basename(newest_cmo_url))
    file.write(f'{datetime.datetime.now()}: A pdf successfully downloaded. \n')
    with open(file_path, 'wb') as f:
        f.write(response.content)
else:
    file.write(f'{datetime.datetime.now()}: the script ran without pdf '
               f'download. \n')
    print(f"Response: {response}")
    print("No PDF found.")

