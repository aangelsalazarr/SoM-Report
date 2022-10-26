import datetime
import requests  # pip install requests
import os
from datetime import date


'''
url: https://www.eia.gov/outlooks/steo/pdf/steo_full.pdf

looking at the url it seems that no url addresses are necessary
'''

seoUrl = 'https://www.eia.gov/outlooks/steo/pdf/steo_full.pdf'

# grabbing today's date to be used in our url_date variable
today = date.today()

# need to convert our date to fit format used in url
today_rfmt = today.strftime("%B_%Y")

output_dir = '.\eia_short_term_energy_outlook'
response = requests.get(seoUrl)

# process to eia seo
if response.status_code == 200:
    file_path = os.path.join(output_dir, str(today_rfmt) + '_'
                             + os.path.basename(seoUrl))
    # file.write(f'{datetime.datetime.now()}: A pdf successfully downloaded.
    # \n')
    with open(file_path, 'wb') as f:
        f.write(response.content)
else:
    # file.write(f'{datetime.datetime.now()}: the script ran without pdf '
               # f'download. \n')
    print(f"Response: {response}")
    print("No PDF found.")