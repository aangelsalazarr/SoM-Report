import datetime
import requests  # pip install requests
import os
from datetime import date

output_dir = '.\jpm_market_recap'

# grabbing today's date to be used in our url_date variable
today = date.today()

# need to convert our date to fit format used in url
today_reformat = today.strftime("%#m-%#d-%y")

wmrUrl = 'https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/insights/market-insights/wmr/weekly_market_recap.pdf'

response = requests.get(wmrUrl)

file = open(r'.\report_processing_log\jpmWMRLogger.txt', 'a')

if response.status_code == 200:
    file_path = os.path.join(output_dir, str(today_reformat) + '_' +
                             os.path.basename(wmrUrl))
    file.write(f'{datetime.datetime.now()}: A pdf successfully downloaded. \n')
    with open(file_path, 'wb') as f:
        f.write(response.content)

else:
    file.write(f'{datetime.datetime.now()}: the script ran without pdf '
               f'download. \n')
    print(f"Response: {response}")
    print("No PDF found.")
