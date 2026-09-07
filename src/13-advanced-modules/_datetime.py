# Trying out the different ways datetime can format and diff dates.
from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time

# import datetime

now = datetime.now()
now = datetime.today()

result = datetime.now()
result = now.year
result = now.month
result = now.day
result = now.hour
result = now.minute
result = now.second

result = datetime.ctime(now)
result = datetime.strftime(now,'%Y')
result = datetime.strftime(now,'%X')
result = datetime.strftime(now,'%d')
result = datetime.strftime(now,'%A')
result = datetime.strftime(now,'%B')
result = datetime.strftime(now,'%Y %B %A')

t = '15 April 2019 hour 10:12:30'
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
result = result.year

birthday = datetime(1983,5,9,12,30,10)

result = datetime.timestamp(birthday) # seconds
result = datetime.fromtimestamp(result) # seconds to datetime
result = datetime.fromtimestamp(0)

result = now - birthday # timedelta

# result = result.days
# result = result.seconds
# result = result.microseconds
print(now)

# result = now + timedelta(days=10)
# result = now + timedelta(days=730, minutes = 10)

result = now - timedelta(days = 10)

print(result)
