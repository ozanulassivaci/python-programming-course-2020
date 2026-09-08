# Trying out the different ways datetime can format and diff dates.
#
# The datetime module represents points in time (dates + times) as objects,
# instead of you juggling separate year/month/day numbers yourself. It also
# knows how to convert those objects to/from text, and how to compute the
# difference between two points in time.
from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time

# import datetime

# datetime.now() returns a datetime object for the current local date and
# time (down to microseconds). datetime.today() does effectively the same
# thing for local time - both exist because of small historical/API reasons,
# but for everyday use they're interchangeable.
now = datetime.now()
now = datetime.today()

result = datetime.now()

# A datetime object stores its components as separate attributes you can
# read individually - no string parsing required.
result = now.year
result = now.month
result = now.day
result = now.hour
result = now.minute
result = now.second

# datetime.ctime(now) formats the datetime using a fixed, C-style layout,
# e.g. "Tue Apr 15 10:12:30 2025".
result = datetime.ctime(now)

# strftime ("string format time") converts a datetime object INTO a string,
# using a template made of "%" codes. Each code stands for one piece of the
# date/time:
#   %Y -> 4-digit year, e.g. 2025
#   %X -> locale's time representation, e.g. 10:12:30
#   %d -> 2-digit day of the month, e.g. 05
#   %A -> full weekday name, e.g. Tuesday
#   %B -> full month name, e.g. April
# You can mix several codes and literal text together in one template, as
# the last line below shows.
result = datetime.strftime(now,'%Y')
result = datetime.strftime(now,'%X')
result = datetime.strftime(now,'%d')
result = datetime.strftime(now,'%A')
result = datetime.strftime(now,'%B')
result = datetime.strftime(now,'%Y %B %A')

t = '15 April 2019 hour 10:12:30'
# strptime ("string parse time") does the reverse of strftime: it converts a
# STRING into a datetime object, using a template that must match the
# string's layout piece for piece. Here '%d %B %Y hour %H:%M:%S' matches
# "15 April 2019 hour 10:12:30" like this:
#   %d    -> 15        (day)
#   %B    -> April     (full month name)
#   %Y    -> 2019       (4-digit year)
#   "hour"-> the literal word "hour" in the string
#   %H:%M:%S -> 10:12:30 (24-hour hour, minute, second)
# The literal text "hour" in the template must appear in the exact same
# place in the string being parsed, or strptime raises a ValueError.
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
result = result.year  # 2019, read off the datetime object we just parsed

birthday = datetime(1983,5,9,12,30,10)

# A "timestamp" (a.k.a. Unix time / epoch time) is a single number: the
# number of seconds elapsed since January 1, 1970 00:00:00 UTC. It's a very
# common way to store/compare/transmit points in time as plain numbers.
result = datetime.timestamp(birthday) # seconds since the epoch, as a float
result = datetime.fromtimestamp(result) # converts that number of seconds back into a datetime
result = datetime.fromtimestamp(0) # timestamp 0 is, by definition, the epoch itself: Jan 1, 1970

# Subtracting one datetime from another gives a timedelta object - a
# DURATION (made of days, seconds, microseconds), not another point in time.
# "now - birthday" answers "how much time has passed between these two dates?"
result = now - birthday # timedelta

# result = result.days
# result = result.seconds
# result = result.microseconds
print(now)

# You can also go the other direction: add or subtract a timedelta from a
# datetime to shift it forward or backward in time.
# result = now + timedelta(days=10)
# result = now + timedelta(days=730, minutes = 10)

# This computes the date and time exactly 10 days before "now".
result = now - timedelta(days = 10)

print(result)
