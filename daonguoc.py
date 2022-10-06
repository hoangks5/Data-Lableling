name_file = 'AAPL Historical Data.csv'
with open(name_file,'r',encoding='utf=8') as f:
    data = f.read().splitlines()
    datanew = data.reverse()
    print(data)
    
    
    
    
    
    
'''     datanew1 = '\n'.join(datanew)
with open(name_file,'w',encoding='utf=8') as f:
    f.write(datanew1)
    f.close() '''