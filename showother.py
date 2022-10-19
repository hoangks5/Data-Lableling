
import pandas as pd

frame = pd.read_csv('t.csv')

dates = list(frame['DATE'])


import datetime as dt


x = [dt.datetime.strptime(d,'%d-%m-%Y').date() for d in dates]
y = list(frame['Value'])

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval = 5000))
plt.plot(x,y)
plt.gcf().autofmt_xdate()
plt.show()
