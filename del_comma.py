path_name = 'BTC_USD.csv'

with open(path_name,'r',encoding='utf-8') as f:
    data = f.read().splitlines()
    
for i in data[1:]:
    j = i.split(',')[1][1:]
    print(j*1000)
    