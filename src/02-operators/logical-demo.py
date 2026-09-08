
# 1- Check whether an entered number is between 0 and 100.
# number = float(input('number: '))
# Both sides need to be True for "and" to be True: the number must be
# above 0 AND at or below 100.
# result = (number > 0) and (number<=100)
# print(f'is the number between 0-100: {result}')

# 2- Check whether an entered number is a positive even number.
# number = int(input('number: '))
# "Positive" and "even" are two independent conditions, joined with "and"
# so BOTH must hold for the overall check to pass.
# result = (number > 0) and (number % 2 == 0)
# print(f'is the entered number a positive even number: {result}')


# 3- Check a login using an email and password.
# email = 'email@ozanulassivaci.com'
# password = 'abc123'

# entered_email = input('email: ')
# entered_password = input('password: ')

# Both the email AND the password must match for a successful login --
# a single wrong field is enough to make the whole "and" expression False.
# result = (entered_email == email) and (entered_password == password)
# print(f'was the login successful: {result}')


# 4- Compare 3 entered numbers by size.
# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))

# a is only the largest if it beats BOTH other numbers -- hence "and".
# result = (a > b) and (a > c)
# print(f'a is the largest number: {result}')

# result = (b > a) and (b > c)
# print(f'b is the largest number: {result}')

# result = (c > a) and (c > b)
# print(f'c is the largest number: {result}')


# 5- Take two midterm grades (%60) and a final grade (%40) from the user and
#    calculate the average. Print "passed" if the average is 50 or above,
#    otherwise print "failed".
#    a-) Even if the average is 50, the final grade must be at least 50.
#    b-) If the final grade is 70 or above, the average doesn't matter.

# midterm1 = float(input('midterm 1: '))
# midterm2 = float(input('midterm 2: '))
# final = float(input('final: '))

# average = ((midterm1+midterm2)/2)*0.6 + (final * 0.4)
# Rule (a): needs BOTH the average to be enough AND the final to be at
# least 50 -- "and" enforces "both conditions required".
# result = (average>=50) and (final>=50)
# Rule (b): passes if EITHER the average is enough OR the final alone was
# 70+ -- "or" enforces "either condition is enough on its own".
# result = (average >=50) or (final>=70)

# print(f"student's average: {average} and pass status: {result}")


# 6- Take a person's name, weight and height, and calculate their BMI.
#    Formula: (weight / height squared)
#    Which category does the person fall into, based on the table below?
#    0-18.4    => Underweight
#    18.5-24.9 => Normal
#    25.0-29.9 => Overweight
#    30.0-34.9 => Obese


name = input('your name: ')
weight_kg = float(input('your weight: '))
height_m = float(input('your height: '))

# BMI formula: weight divided by height squared. "**" is exponentiation,
# so height_m ** 2 means "height squared".
bmi = (weight_kg) / (height_m ** 2)
# Each of these checks a different range with "and": the value must be
# above the range's lower bound AND at/below its upper bound.
is_underweight = (bmi >= 0) and (bmi <= 18.4)
is_normal = (bmi > 18.4) and (bmi <= 24.9)
is_overweight = (bmi > 24.9) and (bmi <= 29.9)
# Careful: this range starts at ">= 29.9" while is_overweight ends at
# "<= 29.9" -- at exactly bmi == 29.9 BOTH is_overweight and is_obese end
# up True at the same time, which is a boundary overlap bug in these
# conditions (the ranges should really meet with one being a strict "<"
# or ">" so they don't share an edge value).
is_obese = (bmi >= 29.9) and (bmi <= 34.9)

print(f'{name} your BMI: {bmi} and are you underweight: {is_underweight}')
print(f'{name} your BMI: {bmi} and are you normal weight: {is_normal}')
print(f'{name} your BMI: {bmi} and are you overweight: {is_overweight}')
print(f'{name} your BMI: {bmi} and are you obese: {is_obese}')
