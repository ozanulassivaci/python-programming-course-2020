# 1- Ask the user for their name, age and education level, and check
#    whether they can get a driver's license. The requirement is being
#    at least 18 and having a high school or university education.

# name = input('your name: ')
# age = int(input('your age: '))
# education = input('education: ')

# Pattern: a nested if, where the inner condition uses "or" -- either
# education value is acceptable, so only ONE of the two needs to be True
# for the "or" to be True. The outer if makes sure we only even ask the
# education question once the age requirement is already satisfied.
# if (age>=18):
#     if (education=='high school' or education=='university'):
#         print(f'{name} you can get a license.')
#     else:
#         print(f"{name} you can't get a license, your education isn't enough.")
# else:
#     print(f"{name} you can't get a license, you're not old enough.")

# 2- Take two written exam grades and one oral grade from a student and
#    print the letter grade that matches the calculated average.
#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

# written1 = float(input('1st written exam: '))
# written2 = float(input('2nd written exam: '))
# oral = float(input('oral exam: '))

# average = (written1 + written2 + oral)/3

# Pattern: an if/elif chain used to bucket a continuous value into named
# ranges, checked from lowest to highest. Each condition combines a lower
# and upper bound with "and" so the average falls into exactly one bucket.
# if (average>=0) and (average<25):
#     print(f'your average: {average} your grade: 0')
# elif (average >= 25 ) and (average<45):
#     print(f'your average: {average} your grade: 1')
# elif (average >= 45 ) and (average<55):
#     print(f'your average: {average} your grade: 2')
# elif (average >= 55 ) and (average<70):
#     print(f'your average: {average} your grade: 3')
# elif (average >= 70 ) and (average<85):
#     print(f'your average: {average} your grade: 4')
# elif (average >= 85 ) and (average<=100):
#     print(f'your average: {average} your grade: 5')
# else:
#     print('you entered invalid info.')




# 3- Calculate a car's next service date based on the date it was
#    first registered.
#    1st service => year 1
#    2nd service => year 2
#    3rd service => year 3
#    ** Calculate the elapsed time in days from the given day, month, year.
#    *** You'll need the datetime module.
#    (now) - (2018/8/1) => days
# The datetime module is part of Python's standard library -- it ships
# with Python, so importing it just makes its tools available, no
# installation needed.
import datetime

date = input('when was your car first registered (2019/8/9): ')
# split('/') breaks the typed date on every '/' character into a list of
# 3 strings, e.g. "2019/8/9" -> ['2019', '8', '9'].
date = date.split('/')
# datetime.datetime(year, month, day) builds a date/time object. Each
# piece has to be converted from string to int first, since the pieces
# from split() are still text.
registration_date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
# datetime.datetime.now() returns the current date and time at the
# moment this line runs.
now = datetime.datetime.now()
# Subtracting one datetime from another gives a timedelta object, which
# represents the span of time between them.
diff = now - registration_date
# .days extracts just the whole number of days from that timedelta.
days = diff.days

# Buckets the elapsed days into 3 yearly service windows. Note: if the
# entered registration date were in the future, `diff` would be negative
# and `days` would be a negative number -- which would still satisfy
# `days <= 365` and incorrectly report "1st service interval" instead of
# flagging the input as invalid. Also, any span beyond 3 years (days >
# 365*3) falls through to the "invalid duration" branch, even though a
# very overdue car isn't really an "invalid" input -- just something this
# simple chain doesn't have a dedicated message for.
if days <= 365:
    print('1st service interval')
elif days > 365 and days <= 365*2:
    print('2nd service interval')
elif days > 365*2 and days <= 365*3:
    print('3rd service interval')
else:
    print('invalid duration.')
