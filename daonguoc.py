name_file = 'BTC_USD Bitfinex Historical Data.csv'
with open(name_file,'r',encoding='utf=8') as f:
    data = f.read().splitlines()
    data.reverse()
    datanew = '\n'.join(data)
with open(name_file,'w',encoding='utf=8') as f:
    f.write(datanew)
    f.close()