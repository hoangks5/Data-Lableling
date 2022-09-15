

import pandas as pd
f=pd.read_csv("vietnam-temperature-from-1901-2015-wb.csv")
keep_col = ['tas','Year','Month']
new_f = f[keep_col]
new_f.to_csv("newFile.csv", index=False)