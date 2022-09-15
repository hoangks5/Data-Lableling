import datetime as dt

x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]