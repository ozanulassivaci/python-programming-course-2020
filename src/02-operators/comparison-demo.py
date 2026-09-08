
# 1- Which of the two entered numbers is bigger?

# a = int(input('a: '))
# b = int(input('b: '))

# ">" is the "greater than" comparison operator; the expression itself
# evaluates to a bool (True/False), which we can store and print directly.
# result = (a > b)
# print(f'a: {a} b: {b} is greater than: {result}')

# 2- Take two midterm grades (%60) and a final grade (%40) from the user and
#    calculate the average. Print "passed" if the average is 50 or above,
#    otherwise print "failed".

# midterm1 = float(input('1st midterm: '))
# midterm2 = float(input('2nd midterm: '))
# final = float(input('final: '))

# The midterms are averaged together first, then weighted 60%, and the
# final is weighted 40% -- a common "weighted average" pattern.
# average = (((midterm1 + midterm2) / 2) * 0.6) + (final * 0.4)

# ">=" ("greater than or equal to") gives the pass/fail bool directly,
# which is then embedded straight into the f-string.
# print(f'your average: {average} and pass status: {average>=50}')

# 3- Print whether an entered number is odd or even.

# number = int(input('number: '))

# "%" (modulo) gives the remainder after division by 2. A remainder of 0
# means the number divides evenly by 2, i.e. it's even.
# is_even = (number % 2 == 0)

# print(f'is the entered number even: {is_even}')

# 4- Print whether an entered number is negative or positive.

# number = int(input('number: '))
# is_positive = (number > 0)

# print(f'is the entered number positive: {is_positive}')

# 5- Ask for an email and password and check if they're correct.
#    (email: email@ozanulassivaci.com password:abc123)

email = 'email@ozanulassivaci.com'
password = 'abc123'

entered_email = input('email: ')
entered_password = input('password: ')

# .lower() and .strip() normalize the entered email before comparing --
# lowercasing avoids failing the check over case differences, and
# stripping removes any accidental leading/trailing spaces the user might
# have typed or pasted in. Note the password check below only lowercases,
# not strips -- so a stray space in the password would still cause a
# mismatch, a subtle asymmetry worth noticing.
is_email = (email == entered_email.lower().strip())
is_password = (password == entered_password.lower())

print(f'Is the email correct: {is_email} and is the password correct: {is_password}')
