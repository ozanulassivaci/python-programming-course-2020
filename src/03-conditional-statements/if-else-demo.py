# 1- Ask the user for their name, age and education level, and check
#    whether they can get a driver's license. The requirement is being
#    at least 18 and having a high school or university education.

# name = input('your name: ')
# age = int(input('your age: '))
# education = input('education: ')

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
import datetime

date = input('when was your car first registered (2019/8/9): ')
date = date.split('/')
registration_date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
now = datetime.datetime.now()
diff = now - registration_date
days = diff.days

if days <= 365:
    print('1st service interval')
elif days > 365 and days <= 365*2:
    print('2nd service interval')
elif days > 365*2 and days <= 365*3:
    print('3rd service interval')
else:
    print('invalid duration.')
