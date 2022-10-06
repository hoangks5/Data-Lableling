name_file = ''
with open(name_file,'r',encoding='utf=8') as f:
    data = f.read().splitlines()
    datanew = data.reverse()
with open(name_file,'w',encoding='utf=8') as f:
    f.write(datanew)
    f.close()