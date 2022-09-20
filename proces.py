
import pandas as pd



path_name = 'BTC_USD.csv'
df = pd.read_csv(path_name)

df_new = df['Date']
print(df_new)