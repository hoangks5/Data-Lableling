
import pandas as pd

frame = pd.read_csv('vietnam-rainfall-from-1901-2015-wb.csv')

dates = list(frame['Month/Year'])


import datetime as dt


x = [dt.datetime.strptime(d,'%m/%Y').date() for d in dates]
y = range(len(x)) # many thanks to Kyss Tao for setting me straight here

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%Y'))
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval = 10000))
plt.plot(x,y)
plt.gcf().autofmt_xdate()
plt.show()