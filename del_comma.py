path_name = 'XAU_USD Historical Data.csv'
with open(path_name,'r',encoding='utf-8') as f:
    data = f.read().splitlines()
    
    
dtt = []
for i in data[1:]:
    j = float(i.split(',')[1][1:])
    k = float(i.split(',')[2][:-1])
    l = j*1000+k
    dtt.append(i.split(',')[0]+','+str(l))
    
neww = '\n'.join(dtt)
with open('new.csv','w',encoding='utf-8') as f:
    f.write(neww)
    f.close()