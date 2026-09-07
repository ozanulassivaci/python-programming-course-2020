salary_ali = 5000
salary_ahmet = 4000
tax = 0.27

print(salary_ali - (salary_ali * tax))
print(salary_ahmet - (salary_ahmet * tax))

# Variable naming rules

# can't start with a digit

number1 = 10
print(number1)

number1 = 20
print(number1)

number1 += 30
print(number1)

# Case sensitivity

age = 20
AGE = 30

print(age)
print(AGE)

# Better to stick with plain ASCII letters in identifiers

year = 20
_age = 20

x = 1                # int
y = 2.3               # float
name = "Kerem"        # string
is_student = True     # bool

# x, y, name, is_student = (1, 2.3, "Kerem", True)

a = '10'
b = '20'
print(a+b)  # => 1020

first_name = "Ozan"
last_name = " Sivaci"

print(first_name + last_name)  # Ozan Sivaci
