fruits = {'orange', 'apple', 'banana'}

# print(fruits[0]) can't be indexed, sets have no order

for x in fruits:
    print(x)

fruits.add('cherry')
fruits.update(['mango', 'grape', 'apple'])

fruits.remove('mango')
fruits.discard('apple')
fruits.pop()

fruits.clear()

print(fruits)

# my_list = [1,2,5,4,4,2,1]
# print(my_list)
# print(set(my_list))
