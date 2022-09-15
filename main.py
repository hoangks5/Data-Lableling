import csv
import numpy
reader = csv.reader(open("test.csv", "rb"), delimiter=",")
x = list(reader)
result = numpy.array(x).astype("float")