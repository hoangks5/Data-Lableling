path_name = 'BTC_USD.csv'

with open(path_name,'r',encoding='utf-8') as f:
    data = f.read().splitlines()
    
    
dtt = []
for i in data[1:]:
    j = float(i.split(',')[1][1:])
    k = float(i.split(',')[2][:-1])
    l = j*1000+k
    dtt.append(i.split(',')[1][1:]+','+str(l))
    