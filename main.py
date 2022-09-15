import csv
import numpy
reader = csv.reader(open("vietnam-rainfall-from-1901-2015-wb.csv", "rb"), delimiter=",")
x = list(reader)
#result = numpy.array(x).astype("float")
print(x)

import pandas as pd
f=pd.read_csv("vietnam-rainfall-from-1901-2015-wb.csv")
keep_col = ['pr','Year','Month']
new_f = f[keep_col]
new_f.to_csv("newFile.csv", index=False)