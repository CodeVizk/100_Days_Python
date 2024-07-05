import datetime as dt

now = dt.datetime.now()
print(now)
print(type(now))

year = now.year
month = now.month
day = now.day
week = now.weekday()
print(week)


dob = dt.datetime(year=2005, month=4, day=27, hour=13)
print(dob)