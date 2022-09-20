
import pandas as pd



path_name = 'BTC_USD.csv'
df = pd.read_csv(path_name)

print(df.to_string()) 
