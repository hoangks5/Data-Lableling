
import pandas as pd

# Lọc cột dữ liệu

path_name = 'XAU_USD Historical Data.csv' 
key_cols = ['Date','Price']
df = pd.read_csv(path_name,usecols=key_cols,skipinitialspace=True)
df.to_csv(path_name,index=False)


