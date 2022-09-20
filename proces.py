
import pandas as pd



path_name = 'BTC_USD.csv' 
key_cols = ['Date','Price']
key_cols['Price']
df = pd.read_csv(path_name,usecols=key_cols,skipinitialspace=True)
df.to_csv(path_name,index=False)