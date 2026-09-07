def say_hello(name='user'):
    return 'Hello ' + name

msg = say_hello('Kerem')
msg = say_hello('Ada')

print(msg)

def total(num1, num2):
    return num1 + num2

result = total(10, 20)
result = total(15, 20)
print(result)

def calculate_age(birth_year):
    return 2019 - birth_year

age_kerem = calculate_age(2017)
age_ada = calculate_age(2010)
age_sena = calculate_age(1999)

print(age_kerem, age_ada, age_sena)

def years_until_retirement(birth_year, name):
    '''
    DOCSTRING: How many years until retirement, based on birth year
    INPUT: Birth year
    OUTPUT: The calculated number of years
    '''
    age = calculate_age(birth_year)
    years_left = 65 - age

    if years_left > 0:
        print(f'{years_left} years left until retirement')
    else:
        print('already retired')


years_until_retirement(1983, 'Ali')
years_until_retirement(1950, 'Ahmet')
years_until_retirement(1974, 'Yagmur')

print(help(years_until_retirement))

list = [1, 2, 3]

print(help(list.append))
