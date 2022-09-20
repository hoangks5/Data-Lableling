
import pandas as pd



path_name = 'BTC_USD.csv' 
key_cols = ['Date','Price']
df = pd.read_csv(path_name,usecols=key_cols,skipinitialspace=True)
df = df.to_string()
df.to_csv(path_name)