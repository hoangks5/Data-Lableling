


with open('XAU_USD.csv','r',encoding='utf-8') as f:
    data = f.read().splitlines()

for i in data:
    last = i.split(',')[2]
    print(last)