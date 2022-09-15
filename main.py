import pandas as pd

read_file = pd.read_excel ('vietnam-rainfall-from-1901-2015-wb.xls')
read_file.to_csv ('e.csv', index = None, header=True)