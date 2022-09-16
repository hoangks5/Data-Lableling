

import pandas as pd
f=pd.read_csv("vietnam-temperature-from-1901-2015-wb.csv")
keep_col = ['Month','Year']
new_f = f[keep_col]
for new in new_f:
    print(new)