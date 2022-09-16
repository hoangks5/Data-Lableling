


with open("vietnam-temperature-from-1901-2015-wb.csv",'r',encoding='utf-8') as f:
    data = f.read().splitlines()

for i in data:
    nb = i.split(',')[0]
    timest = i.split(',')[2]+'/'+i.split(',')[1]
    string = timest + ',' + nb
    print(string)