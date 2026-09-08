# A set is an unordered collection of UNIQUE items, written with curly
# braces (like a dict, but with just values, no keys). Duplicates are
# automatically dropped, and there is no guaranteed order to the items.
fruits = {'orange', 'apple', 'banana'}

# print(fruits[0]) can't be indexed, sets have no order
# Since a set has no positions/order, square-bracket indexing doesn't make
# sense for it and raises a TypeError -- there is no "item 0" of a set.

# You can still visit every item with a for loop; you just can't predict
# or rely on the order they'll come out in (it may even differ between
# runs).
for x in fruits:
    print(x)

# add() inserts a single new item. If the value is already present,
# add() silently does nothing (sets never contain duplicates).
fruits.add('cherry')
# update() merges in every item from another collection (here a list) --
# similar to how extend() works for lists, but duplicates ('apple' is
# already in the set) are automatically ignored.
fruits.update(['mango', 'grape', 'apple'])

# remove(value) deletes that item; it raises a KeyError if the value
# isn't in the set.
fruits.remove('mango')
# discard(value) also deletes that item, but does NOT raise an error if
# the value is missing -- the safer choice when you're not sure the item
# is there.
fruits.discard('apple')
# pop() removes and returns an ARBITRARY item, since a set has no defined
# "first" or "last" element to remove the way a list does.
fruits.pop()

# clear() empties the set in place.
fruits.clear()

print(fruits)  # set() -- Python prints an empty set as set(), because
               # {} on its own would be ambiguous with an empty dict

# A very common use for sets: removing duplicates from a list. Converting
# a list to a set keeps only the unique values (order is not preserved).
# my_list = [1,2,5,4,4,2,1]
# print(my_list)
# print(set(my_list))     # would print {1, 2, 4, 5} in some order
