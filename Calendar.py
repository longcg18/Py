from datetime import datetime
import pytz

#print (calendar.TextCalendar(firstweekday=6).formatyear(2023))

#mm, dd, yyyy = input().split(' ')

#d = date(year=int(yyyy), month=int(mm), day=int(dd))

#print(date())

#print(calendar.day_name[d.weekday()].upper())

dt_us_central = datetime.now(pytz.timezone('America/Mexico_City'))
print("US Central DateTime:", dt_us_central.strftime("%Y:%m:%d %H:%M:%S %Z %z"))
