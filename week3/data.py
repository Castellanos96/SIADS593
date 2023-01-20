import os 
import pandas as pd
from urllib.request import urlretrieve 
#test line 

URL = 'https://raw.githubusercontent.com/Castellanos96/SIADS593/main/Items.csv'

def get_data(filename='Items.csv', url=URL, force_download=False):
    if force_download or not os.path.exists(filename):
        urlretrieve(URL, filename)
    return pd.read_csv('Items.csv',index_col=0)
