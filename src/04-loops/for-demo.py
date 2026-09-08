numbers = [1, 3, 5, 7, 9, 12, 19, 21]

# 1- Which numbers in the list are multiples of 3?
# "for item in some_list:" runs its indented block once per element,
# with `item` (here `number`) bound to the current element each time.
# for number in numbers:
#     if (number%3==0):
#         print(number)

# 2- What is the sum of the numbers in the list?

# A running total pattern: start an accumulator at 0 before the loop,
# then add to it on every iteration.
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

# len(city) gives the character count of each string as the loop visits it.
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
# Looping over a list of dicts: each `product` is one dict, and
# product['price'] reads its 'price' key. The prices are stored as
# STRINGS here, so int(...) converts each one to a number before adding
# it to the running total -- skipping that conversion would try to "add"
# strings together and either fail or concatenate instead of summing.
# total = 0
# for product in products:
#     price = int(product['price'])
#     total += price
# print('total product price: ', total)


# 6- Show the products priced at most 5000.

# for product in products:
#     if (int(product['price']) <= 5000):
#         print(product['name'])
