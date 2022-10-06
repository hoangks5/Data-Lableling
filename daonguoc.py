name_file = 'AAPL Historical Data.csv'
with open(name_file,'r',encoding='utf=8') as f:
    data = f.read().splitlines()
    datanew = data.reverse()
    datanew = '\n'.join(datanew)
with open(name_file,'w',encoding='utf=8') as f:
    f.write(datanew)
    f.close()