


with open("vietnam-rainfall-from-1901-2015-wb.csv",'r',encoding='utf-8') as f:
    data = f.read().splitlines()

t = []
for i in data:
    nb = i.split(',')[0]
    timest = i.split(',')[2]+'/'+i.split(',')[1]
    string = timest + ',' + nb
    t.append(string) 
st = '\n'.join(t)
with open("vietnam-rainfall-from-1901-2015-wb.csv",'w',encoding='utf-8') as f:
    f.write(st)
    f.close()