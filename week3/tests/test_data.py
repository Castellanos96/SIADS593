import pandas as pd 
from data import get_data

def check_features():
    data = get_data()
    assert all(data.columns == ['Item','Weight','Survival Points'])
