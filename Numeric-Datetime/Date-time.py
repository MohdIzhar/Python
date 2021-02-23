# Based on Proleptic Gregorian calendar
# Use with care with historical dates
# Last country to adopt the Gregorian calendar was Saudi Arabia in 2016

# Timezones :- Naive vs Aware

# Naive - lacks timezone and daylight saving time information
# Aware - They carry information about timezone and daylight saving time

# dates, time, datetime, timedelta, zoneinfo are immutable

import datetime
from time import time
print(datetime.date(2020,1, 6))
# year, month and day are specified in order of descending size of unit duration,
print(datetime.date(year = 2014, month=1, day=6))


# current date
print(datetime.date.today())

# getting date from seconds
print(datetime.date.fromtimestamp(1000000000))

# using Ordinal Constructor which accepts integer number of days
#  starting with one on the first of january in year one.
# Assuming Gregorian calender extends back far (starts from 1901)
print(datetime.date.fromordinal(720669))

# value can extracted like year, month, day
d = datetime.date.today()
print(d.year)
print(d.month)
print(d.day)

# To get the weekday we have special method that return weekday
# in range 0-6 (both inclusive)
print(d.weekday())
# where monday is zero and sunday is six

# ISO based system uses 1 as Monday and Sunday as 7
print(d.isoweekday())

# isoformat date returns in string
print(d.isoformat())

# string format placeholder
            #   +--> Weekday in alphabet form
            #   |  +---> int date
            #   |  |   +--> Month
            #   |  |   |  +---> Year
            #   |  |   |  |
f = d.strftime('%A %d %B %Y')
print(f)

s = "The date is {:%A %d %B %Y}".format(d)
print(s)
# more format holder refer to python documentation

# Note string formatter may behave different for different operating system
# So, the best optimal solution is extract each format spcifier separately
# the more powerful and portable
st = "{date:%A} {date.day} {date:%B} {date.year}".format(date=d)
print(st)

# min and max attributes of datetime module
mn = datetime.date.min
mx = datetime.date.max
print(mn)
print(mx)


# Time function takes argument as
# hours, minutes, seconds, microseconds

t = datetime.time(3,1,2,232)
print(t)

# for better understanding use keyword arguments

print(datetime.time(hour=23, minute=59, second=59, microsecond=999999))
# all values are zero based integer as the date were were 1 based
# the above value represent the last instances of day

print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)

# isoformat can also be obtained
print(t.isoformat())
# same with strformat method
print(t.strftime('%Hh%Mm%Ss'))
# best approach use of format
print("{t.hour}h {t.minute}m {t.second}s".format(t=t))

# Composite Date and Time
from datetime import date, datetime
# now datetime refers to class rather than module as earier

# now time refers to the 
print(datetime.time)

# so to avoid confusion alias them as

from datetime import datetime as Datetime
import datetime as dt
import datetime

print(datetime.datetime(year=2021, month=1, day=25, hour=22, minute=47, second=41, microsecond=245873))

# today
print(datetime.datetime.today())

# now method
print(datetime.datetime.now())
# the above two methods return localtime as per your machine

# Current Universal Time
print(datetime.datetime.utcnow())

# support ordinal and fromtimestamp
print(datetime.datetime.fromordinal(5))
print(datetime.datetime.fromtimestamp(3635352))
print(datetime.datetime.utcfromtimestamp(3635352))

# we can combine time

d = datetime.date.today()
t = datetime.time(8,15)
print(datetime.datetime.combine(d,t))


# to parse string datetime

ds = datetime.datetime.strptime("Monday 6 January 2014, 12:13:31", "%A %d %B %Y, %H:%M:%S")
print(ds)

# to get the specific date and time from ds use date and time method
print(ds.time())
print(ds.date())
print(ds.day)

# timdelta :- strongly recommended to use keyword arguments
# it will combine the all argument and give you the single result
print(datetime.timedelta(milliseconds=1, microseconds=1000))

td = datetime.timedelta(days=7, seconds=125, milliseconds=5500)
print(td.days)
print(td.seconds)
print(td.microseconds)
print(td)

# now extra str function is provided by timdelta
# we can use str as we have already seen repr output
print(str(td))


# Subtracting two datetime yields timedelta

a = datetime.datetime(year=2014, month=5, day=8, hour=14, minute=22)
b = datetime.datetime(year=2014, month=3, day=14, hour=12, minute=9)

diff = a - b
print(diff)
print(diff.total_seconds())

# adding the datetime and timedelta

print(datetime.date.today() + datetime.timedelta(weeks=1)*3)

# Arithmetic on simple timeobject is not supported
f = datetime.time(14,30,0)
g = datetime.time(15,45,0)
# print(f-g)

# TIMEZONES
#  to get timezone we much attach the instances of a TZ info object to our time values
# you can use thirdy party data pytz or dateutil

# tzinfo classes are abstract so can't be instantiated directly

cet = datetime.timezone(datetime.timedelta(hours=1), "CET")
print(cet)

departure = datetime.datetime(year=2021, month=1, day=25, hour=11, minute=13, second=11, tzinfo=cet)
print(departure)
arrival = datetime.datetime(year=2021, month=1, day=25, hour=13, minute=5, second=0, tzinfo=datetime.timezone.utc)
print(arrival)

print(arrival - departure)

# for more info refer to doc or use thirdy party tools
