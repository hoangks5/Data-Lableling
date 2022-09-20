
import pandas as pd



path_name = 'XAU_USD.csv'
df = pd.read_csv(path_name)

print(df.to_string()) 
