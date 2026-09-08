# `def` defines a function. `name='user'` gives the `name` parameter a
# DEFAULT value, used only when the caller doesn't supply that argument
# -- so this function can be called either as say_hello() (using 'user')
# or say_hello('Kerem') (overriding the default).
def say_hello(name='user'):
    # `return` sends a value back to the caller and immediately ends the
    # function -- nothing after a return statement in the same branch runs.
    return 'Hello ' + name

msg = say_hello('Kerem')  # 'Hello Kerem'
msg = say_hello('Ada')    # 'Hello Ada' -- overwrites the previous msg

print(msg)  # Hello Ada

def total(num1, num2):
    return num1 + num2

result = total(10, 20)  # 30
result = total(15, 20)  # 35 -- overwrites the previous result
print(result)  # 35

def calculate_age(birth_year):
    return 2019 - birth_year

# Calling the same function multiple times with different arguments,
# storing each separate result in its own variable.
age_kerem = calculate_age(2017)  # 2
age_ada = calculate_age(2010)    # 9
age_sena = calculate_age(1999)   # 20

print(age_kerem, age_ada, age_sena)  # 2 9 20

def years_until_retirement(birth_year, name):
    '''
    DOCSTRING: How many years until retirement, based on birth year
    INPUT: Birth year
    OUTPUT: The calculated number of years
    '''
    # A function can call another function -- calculate_age is reused
    # here instead of repeating its logic.
    age = calculate_age(birth_year)
    years_left = 65 - age

    if years_left > 0:
        print(f'{years_left} years left until retirement')
    else:
        print('already retired')


# birth_year=1983 -> age 36 -> 65-36 = 29 years left
years_until_retirement(1983, 'Ali')
# birth_year=1950 -> age 69 -> 65-69 = -4, not > 0, so "already retired"
years_until_retirement(1950, 'Ahmet')
# birth_year=1974 -> age 45 -> 65-45 = 20 years left
years_until_retirement(1974, 'Yagmur')

# help() is a built-in that prints a function's docstring (and its
# signature) to the console -- a quick way to read documentation without
# leaving your editor/terminal. help() itself returns None (it just
# prints as a side effect), so wrapping it in print() additionally prints
# the word "None" right after the docstring output.
print(help(years_until_retirement))

list = [1, 2, 3]

# help() works on built-in methods too, showing their documentation --
# handy for exploring what a method does and what arguments it takes
# without searching online. Same as above, this also prints "None"
# afterward since help() returns nothing itself.
print(help(list.append))
