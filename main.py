

import pandas as pd
f=pd.read_csv("vietnam-temperature-from-1901-2015-wb.csv")
keep_col = ['Month','Year']
for i in keep_col:
    print(i)