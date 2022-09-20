
import pandas as pd



path_name = 'BTC_USD.csv' 
key_cols = ['Date','Price']
df = pd.read_csv(path_name,usecols=key_cols)

print(df)