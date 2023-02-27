import os
import null
from black_box import eia_data_processor

# loading our API key
apiKey = os.environ.get('eiaAPI')

# world liquid fuels production and consumption balance
world_liq_prod_cons = {
    "frequency": "monthly",
    "data": [
        "value"
    ],
    "facets": {
        "seriesId": [
            "PAPR_WORLD",
            "PATC_WORLD"
        ]
    },
    "start": null,
    "end": null,
    "sort": [
        {
            "column": "period",
            "direction": "desc"
        }
    ],
    "offset": 0,
    "length": 5000
}

