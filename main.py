import csv
import numpy
reader = csv.reader(open("vietnam-rainfall-from-1901-2015-wb.csv", "rb"), delimiter=",")
x = list(reader)
#result = numpy.array(x).astype("float")
print(x)