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
customer_first_name = 'Ali'
customer_last_name = 'Yilmaz'
customer_full_name = customer_first_name + ' ' + customer_last_name
print(customer_full_name)
customer_gender = True  # Male
customer_national_id = '13165465445'
customer_birth_year = 1989
customer_address = 'Istanbul Kadikoy'
customer_age = 2019 - customer_birth_year

"""
    2- Calculate the total of the following orders.

    Order 1 => 110    TL
    Order 2 => 1100.5 TL
    Order 3 => 356.95 TL
"""
order1 = 110
order2 = 1100.5
order3 = 356.95

total = order1 + order2 + order3

print("Total:", total)
