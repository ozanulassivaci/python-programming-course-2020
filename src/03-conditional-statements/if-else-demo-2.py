'''
1- Check whether an entered number is between 0 and 100.

number = float(input('number: '))

if (number > 0) and (number<=100):
    print('the number is between 0-100.')
else:
    print('the number is not between 0-100.')

'''

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
