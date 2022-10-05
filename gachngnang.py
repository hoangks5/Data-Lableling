import regex as re


name_file = 'AAPL Historical Data.csv'
with open(name_file,'r',encoding='utf-8') as f:
    data = f.read()
convert = re.sub(data,'/','-')