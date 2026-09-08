names = ['Ali', 'Yagmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

# 1-  Add "Cenk" to the end of the list.
# append() mutates the list in place (it doesn't return a new list) and
# always adds exactly one item, at the very end.
# names.append('Cenk')

# 2-  Add "Sena" to the front of the list.
# insert(index, value) puts value at the given position, shifting every
# existing item at or after that position one slot to the right.
# names.insert(0, 'Sena')
# insert(-1, ...) inserts BEFORE the last element (negative indices count
# from the end), which is a common point of confusion -- it does NOT
# append to the very end the way -1 indexing for *reading* would suggest.
# names.insert(-1, 'Mehmet')
# Using len(names) as the index inserts exactly at the end -- equivalent
# to append() in this case, since there's no valid index past the end to
# shift out of the way.
# names.insert(len(names), 'Mehmet')

# 3-  Remove "Deniz" from the list.
# remove(value) searches for the first item equal to value and deletes
# it. It raises a ValueError if the value isn't found anywhere in the list.
# names.remove('Deniz')
# pop() with no argument removes and returns the LAST item.
# names.pop()
# pop(index) removes and returns the item at that specific position.
# names.pop(1)

# 4-  What is the index of "Deniz"?
# index(value) returns the position of the first matching item (also
# raises ValueError if it's missing).
# index = names.index('Deniz')
# names.pop(index)

# 5-  Is "Ali" an element of the list?
# The "in" operator checks membership and gives back True/False directly
# -- much more direct than searching for an index just to check existence.
# result = 'Ali' in names
# result = names.index('Ali')

# 6-  Reverse the list elements.
# reverse() flips the order of all items in place; it doesn't sort them,
# just reverses whatever order they were already in.
# names.reverse()

# 7-  Sort the list elements alphabetically.
# sort() reorders the list in place (there's also sorted(names), which
# returns a new sorted list and leaves the original untouched).
# names.sort()

# 8-  Sort the years list numerically.
# sort() adapts to the item type automatically: numbers sort by value.
# years.sort()

# 9-  Turn the string "Chevrolet,Dacia" into a list.
# text = "Chevrolet,Dacia"
# split(',') breaks a string into a list of pieces wherever the given
# separator occurs, discarding the separator itself.
# result = text.split(',')

# 10- What are the min and max values in years?
# min()/max() are built-in functions (not list methods) that work on any
# sequence of comparable values.
# smallest = min(years)
# largest = max(years)
# print(smallest, largest)

# 11- How many times does 1998 appear in years?
# count(value) tells you how many elements are equal to value.
# result = years.count(1998)

# 12- Clear every element from years.
# clear() empties the list in place, leaving it as [] -- the variable
# still refers to the same (now-empty) list object.
# years.clear()

# 13- Store 3 car brands entered by the user in a list.

brands = []

# Learned that append() only adds one item at a time - extend() is
# the one you'd want for merging whole lists together.
brand = input("brand: ")
brands.append(brand)

brand = input("brand: ")
brands.append(brand)

brand = input("brand: ")
brands.append(brand)

print(brands)
