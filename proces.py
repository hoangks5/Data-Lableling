
import pandas as pd



path_name = 'XAU_USD.csv'
df = pd.read_csv(path_name)

print(df.to_string()) 

with open(path_name,'r',encoding='utf-8') as f:
    data = f.read().splitlines()

datanew = data['Date']

print(datanew)
''' dtt = []
for i in data[1:]:
    gia = i.split(',')[1]
    dt = i.split(',')[0][1:-1]+','+gia
    dtt.append(dt)
save = '\n'.join(dtt)
with open(path_name,'w',encoding='utf-8') as f:
    f.write(save)
    f.close() '''