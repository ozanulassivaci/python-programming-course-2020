numbers = [1, 3, 5, 7, 9, 12, 19, 21]

# 1: Print the numbers list using while.

# Unlike a for loop, a while loop needs you to manage the index yourself:
# start a counter at 0, keep going while it's still a valid index
# (i < len(numbers)), and manually increment it each pass.
# i = 0
# while (i < len(numbers)):
#     print(numbers[i])
#     i += 1

# 2: Take a start and end value from the user and print every odd
#    number in between.

# start = int(input('start: '))
# end = int(input('end: '))

# i = start
# while i < end:
#     i += 1
#     if (i % 2 == 1):
#         print(i)

# 3: Print the numbers from 1 to 100 in descending order.

# Counting DOWN with a while loop: start at the high end and subtract 1
# each iteration until the condition (i > 0) becomes False.
# i = 100
# while i > 0:
#     print(i)
#     i -= 1

# 4: Print 5 numbers entered by the user, sorted.

# A "count-controlled" while loop: keep looping exactly 5 times by
# comparing a counter (i) against a fixed limit.
# numbers = []
# i = 0
# while i<5:
#     number = int(input('number: '))
#     numbers.append(number)
#     i+=1
# numbers.sort()
# print(numbers)

# 5: Store an unlimited number of products entered by the user in a
#    products list.
#    ** Ask the user how many products there will be.
#    ** Each item should be a dict shaped like (name, price).
#    ** Once done adding products, list them all with a while loop.

products = []

count = int(input("how many products do you want to add: "))
i = 0

# Same count-controlled pattern as exercise 4: loop exactly `count` times,
# building up a dict for each product and appending it to the list.
while (i < count):
    name = input('product name: ')
    price = input('product price: ')
    products.append({
        'name': name,
        'price': price
    })
    i += 1

# Even though the exercise says "list them all with a while loop", a
# regular for loop is used here to display the results -- functionally
# it iterates over every dict in products the same way a while loop
# indexing into products would.
for product in products:
    print(f'product name: {product["name"]} product price: {product["price"]}')
