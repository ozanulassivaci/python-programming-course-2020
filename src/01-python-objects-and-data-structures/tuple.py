# Careful: naming variables `list` and `tuple` shadows Python's own
# built-in list() and tuple() functions/types for the rest of this file --
# it still works here since we never need the real built-ins afterward,
# but it's generally best to avoid reusing built-in names for your own
# variables.
list = [1, 2, 3]
# A tuple looks like a list but uses parentheses instead of square
# brackets, and -- crucially -- is IMMUTABLE: once created, you cannot
# add, remove, or change its items.
tuple = (1, 'two', 3)

# print(type(list))   # <class 'list'>
# print(type(tuple))  # <class 'tuple'>

# print(list[2])   # indexing works the same way as lists: 3
# print(tuple[2])  # 3

# print(len(tuple))  # 3
# print(len(list))   # 3

list = ['ali', 'veli']
tuple = ('damla', 'ayse', 'ayse')
# "+" concatenates two tuples into a new tuple, just like it does for
# lists -- the items from the left tuple come first, then the right
# tuple's items, in order.
# ('demet', 'emel', 'ayse') + ('damla', 'ayse', 'ayse')
#   -> ('demet', 'emel', 'ayse', 'damla', 'ayse', 'ayse')
names = ('demet', 'emel', 'ayse') + tuple

print(names)

# Lists ARE mutable, so assigning to an index works fine here.
# list becomes ['ahmet', 'veli'].
list[0] = 'ahmet'
# tuple[0] = 'deniz'
# This is commented out because it would raise a TypeError: tuples don't
# support item assignment at all -- there is no way to change a tuple's
# contents once it's created, which is the whole point of using one when
# you want data that can't accidentally be modified later.

# Tuples support several of the same read-only methods lists do:
print(tuple.count('ayse'))  # 2 -- 'ayse' appears twice in ('damla','ayse','ayse')
print(tuple.index('ayse'))  # 1 -- the first 'ayse' is at index 1

print(list)   # ['ahmet', 'veli']
print(tuple)  # ('damla', 'ayse', 'ayse') -- unchanged, as expected
