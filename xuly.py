


with open('XAU_USD.csv','r',encoding='utf-8') as f:
    data = f.read().splitlines()

dtt = []
for i in data[1:]:
    last = float(i.split(',')[2][:-1])
    firt = float(i.split(',')[1][1:])*1000
    gia = str(last + firt)
    dt = i.split(',')[0]+','+gia
    dtt.append(dt)
