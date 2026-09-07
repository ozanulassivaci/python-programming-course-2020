numbers = [1, 3, 5, 7, 9, 12, 19, 21]

# 1- Which numbers in the list are multiples of 3?
# for number in numbers:
#     if (number%3==0):
#         print(number)

# 2- What is the sum of the numbers in the list?

# total = 0
# for number in numbers:
#     total += number
# print('total:', total)

# 3- Square the odd numbers in the list.

# for number in numbers:
#     if (number % 2 == 1):
#         print(number ** 2)


cities = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']

# 4- Which cities have at most 5 characters?

# for city in cities:
#     if (len(city) <= 5):
#         print(city)

products = [
    {'name': 'samsung S6', 'price': '3000'},
    {'name': 'samsung S7', 'price': '4000'},
    {'name': 'samsung S8', 'price': '5000'},
    {'name': 'samsung S9', 'price': '6000'},
    {'name': 'samsung S10', 'price': '7000'}
]

# 5- What is the total price of all products?
# total = 0
# for product in products:
#     price = int(product['price'])
#     total += price
# print('total product price: ', total)


# 6- Show the products priced at most 5000.

# for product in products:
#     if (int(product['price']) <= 5000):
#         print(product['name'])
