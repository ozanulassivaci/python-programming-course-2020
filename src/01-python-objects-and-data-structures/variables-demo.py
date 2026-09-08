"""
    1- Create a variable for each of the following pieces of info about a customer.

    Customer first name
    Customer last name
    Customer full name (first + last)
    Customer gender
    Customer national id
    Customer birth year
    Customer address
    Customer age
"""
# A triple-quoted string like the one above can span multiple lines. When
# it appears as a standalone statement (not assigned to anything) it's
# commonly used as a comment block / docstring describing the exercise.

customer_first_name = 'Ali'
customer_last_name = 'Yilmaz'
# Building a full name by concatenating (joining with +) the first name,
# a literal space, and the last name.
customer_full_name = customer_first_name + ' ' + customer_last_name
print(customer_full_name)
customer_gender = True  # Male -- using a bool here as a simple stand-in flag
customer_national_id = '13165465445'  # stored as a string, not a number,
# because we'll never do arithmetic on an ID and leading zeros would be
# lost if it were an int
customer_birth_year = 1989
customer_address = 'Istanbul Kadikoy'
# Ordinary integer subtraction: a fixed reference year minus the birth
# year gives an approximate age. 2019 - 1989 = 30.
customer_age = 2019 - customer_birth_year

"""
    2- Calculate the total of the following orders.

    Order 1 => 110    TL
    Order 2 => 1100.5 TL
    Order 3 => 356.95 TL
"""
order1 = 110       # int
order2 = 1100.5    # float
order3 = 356.95    # float

# Adding an int and floats together automatically produces a float --
# Python "widens" the int to a float so no precision is lost.
# 110 + 1100.5 + 356.95 = 1567.45
total = order1 + order2 + order3

# print() can take several comma-separated arguments; it prints each one
# separated by a single space automatically, so no manual string-building
# is needed here.
print("Total:", total)
