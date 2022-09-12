from pycaiso.oasis import Node
from datetime import datetime
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)


'''
Get locational marginal prices (LMPs) in Day Ahead Marker (DAM) for arbitrary
Nodes and Period. Default = DAM but you can set market parameter in get_lmps to
"RTM" or "RTPD"

Alternatively you can use pre-built Nodes for major aggregated pricing nodes
(apnodes) like SP15
'''

sp15 = Node.SP15()
sp15_lmps = sp15.get_lmps(datetime(2021, 1, 1), datetime(2021, 1, 2))
print(sp15_lmps)
