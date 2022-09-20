


""" with open('Dầu_Thô_WTI.csv','r',encoding='utf-8') as f:
    data = f.read().splitlines()

dtt = []
for i in data[1:]:
    last = float(i.split(',')[2][:-1])
    firt = float(i.split(',')[1][1:])*1000
    gia = str(last + firt)
    dt = i.split(',')[0]+','+gia
    dtt.append(dt)
save = '\n'.join(dtt)
with open('Dầu_Thô_WTI.csv','w',encoding='utf-8') as f:
    f.write(save)
    f.close() """


path_name = 'XAU_USD.csv'


with open(path_name,'r',encoding='utf-8') as f:
    data = f.read().splitlines()

datanew = data['Date','Price']

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