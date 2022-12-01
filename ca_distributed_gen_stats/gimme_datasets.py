import requests
import os

# dictionary containing data sets with url/names
gdgs = {
    'interconnection_rule21_projects/': 'Interconnected Project Sites',
    'interconnection_rule_21_applications/': 'Interconnected Applications',
    'somah/': 'SOMAH Program',
    'csi_working_data_set/': 'California Solar Incentive',
    'low_income/': 'Low-Income Solar PV'
}


def gimme_gdgs_pls(dict,  output_dir='./data_files'):

    # base url for Cali Distro Gen stats
    base_url = 'https://wwww.californiadgstats.gov/download/'

    # creating lists of key, values
    dict_keys = list(dict.keys())
    dict_vals = list(dict.values())

    for key in dict_keys:
        url = base_url + key
        response = requests.get(url=url)

        if response.status_code == 200:
            file_path = os.path.join(output_dir,
                                     os.path.basename(url))

            with open(file_path, 'wb') as f:
                f.write(response.content)

        else:

            print('error :(')


gimme_gdgs_pls(dict=gdgs)


