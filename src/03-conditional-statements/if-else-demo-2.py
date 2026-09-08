# This whole file is a set of worked exercises kept as triple-quoted
# strings (''' ... '''), so none of the code inside them actually runs --
# they act like big multi-line comments/notes you can read through and
# copy out to try individually. Each block below solves one exercise; the
# short note above each one explains the pattern it's demonstrating.

# Pattern: a single "and"-combined condition inside one if/else -- both
# sides of "and" must be True for the number to count as "between 0-100".
'''
1- Check whether an entered number is between 0 and 100.

number = float(input('number: '))

if (number > 0) and (number<=100):
    print('the number is between 0-100.')
else:
    print('the number is not between 0-100.')

'''

# Pattern: a NESTED if -- an if statement placed inside another if's
# block. The inner check (odd/even) only even gets evaluated once the
# outer check (positive) has already passed; this is a different way to
# express "positive AND even" compared to writing one combined condition
# with "and".
'''
2- Check whether an entered number is a positive even number.

number = int(input('number: '))

if (number > 0):
    if (number % 2 ==0):
        print('the entered number is a positive even number.')
    else:
        print('the entered number is positive but odd.')
else:
    print('the entered number is negative.')

'''


# Pattern: nested if/else again, this time to give a DIFFERENT error
# message depending on which specific thing was wrong (email vs
# password) -- something a single combined "and" condition couldn't do,
# since it would only tell you the overall pass/fail, not which part
# failed.
'''
3- Check a login using an email and password.

email = 'email@ozanulassivaci.com'
password = 'abc123'

entered_email = input('email: ')
entered_password = input('password: ')

if (entered_email == email):
    if (entered_password == password):
        print('login successful.')
    else:
        print('your password is wrong')
else:
    print('your email is wrong')


'''


# Pattern: an if/elif/elif chain used to find "the largest of three",
# each branch combining two ">" comparisons with "and" -- a value only
# counts as the largest if it beats BOTH of the other two.
'''
4- Compare 3 entered numbers by size.

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if (a > b) and  (a > c):
    print(f'a is the largest number.')
elif (b > a) and (b > c):
    print(f'b is the largest number.')
elif (c > a) and (c > b):
    print(f'c is the largest number.')

'''

# Pattern: the same rule can be expressed two different but equivalent
# ways -- "case-1" nests the final-grade check inside the average check,
# while "case-2" restructures it as an if/else with the final-grade check
# nested in the else branch. Both end up implementing rule (a): pass only
# if the average is high enough AND the final grade is at least 50.
'''
5- Take two midterm grades (%60) and a final grade (%40) from the user and
   calculate the average. Print "passed" if the average is 50 or above,
   otherwise print "failed".
   a-) Even if the average is 50, the final grade must be at least 50.
   b-) If the final grade is 70 or above, the average doesn't matter.

midterm1 = float(input('midterm 1: '))
midterm2 = float(input('midterm 2: '))
final = float(input('final: '))

average = ((midterm1+midterm2)/2)*0.6 + (final * 0.4)

result = (average>=50) and (final>=50)
result = (average >=50) or (final>=70)

** case-1

if (average>=50):
    if (final>=50):
        print(f"student's average: {average} and pass status: passed")
    else:
        print(f"student's average: {average} and pass status: failed. You need at least 50 on the final.")
else:
    print(f"student's average: {average} and pass status: failed")

** case-2

if (average >=50):
    print(f"student's average: {average} and pass status: passed")
else:
    if (final>=70):
        print(f"student's average: {average} and pass status: passed. You passed by scoring at least 70 on the final.")
    else:
        print(f"student's average: {average} and pass status: failed")


'''

# Pattern: an if/elif/elif/elif/else chain that buckets a continuous
# numeric value (bmi) into named ranges -- each elif only gets checked if
# every condition above it was False, so writing `(bmi>18.4)` here is
# enough (we already know bmi isn't <=18.4, or we wouldn't have reached
# this branch), even though the previous file's version used the fuller
# `(bmi > 18.4) and (bmi <= 24.9)` form for the same idea.
'''

6- Take a person's name, weight and height, and calculate their BMI.
   Formula: (weight / height squared)
   Which category does the person fall into, based on the table below?
   0-18.4    => Underweight
   18.5-24.9 => Normal
   25.0-29.9 => Overweight
   30.0-34.9 => Obese






name = input('your name: ')
weight_kg = float(input('your weight: '))
height_m = float(input('your height: '))

bmi = (weight_kg) / (height_m ** 2)

if (bmi >= 0) and (bmi<=18.4):
    print(f'{name} your BMI: {bmi} and you are underweight.')
elif (bmi>18.4) and (bmi<=24.9):
    print(f'{name} your BMI: {bmi} and you are normal weight.')
elif (bmi>24.9) and (bmi<=29.9):
    print(f'{name} your BMI: {bmi} and you are overweight.')
elif (bmi>=29.9) and (bmi<=45.9):
    print(f'{name} your BMI: {bmi} and you are obese.')
else:
    print('your info is invalid.')

'''
