
import pandas as pd

frame = pd.read_csv('XAU_USD Historical Data.csv')

dates = list(frame['Date'])


import datetime as dt


x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]
y = list(frame['Price'])

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval = 500))
plt.plot(x,y)
plt.gcf().autofmt_xdate()
plt.show()
