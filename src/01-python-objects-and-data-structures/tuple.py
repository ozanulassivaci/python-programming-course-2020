list = [1, 2, 3]
tuple = (1, 'two', 3)

# print(type(list))
# print(type(tuple))

# print(list[2])
# print(tuple[2])

# print(len(tuple))
# print(len(list))

list = ['ali', 'veli']
tuple = ('damla', 'ayse', 'ayse')
names = ('demet', 'emel', 'ayse') + tuple

print(names)

list[0] = 'ahmet'
# tuple[0] = 'deniz'

print(tuple.count('ayse'))
print(tuple.index('ayse'))

print(list)
print(tuple)
