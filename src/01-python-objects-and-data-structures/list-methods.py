numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

# min()/max() are built-in functions that scan a whole sequence and return
# the smallest/largest item. For numbers they compare by value; for
# strings they compare alphabetically (technically by character codes).
val = min(numbers)  # 1
val = max(numbers)  # 16
val = max(letters)  # 'y' -- comes after all the other letters alphabetically
val = min(letters)  # 'a'

# Slicing a list works exactly like slicing a string: [start:stop] takes
# items from index start up to (not including) index stop.
val = numbers[3:6]  # indices 3,4,5 -> [16, 4, 9]
val = numbers[:3]   # from the start -> [1, 10, 5]
val = numbers[4:]   # to the end -> [4, 9, 10]

# Unlike strings, lists ARE mutable -- you can change an element in place
# by assigning to its index. This replaces the 16 (at index 4) with 40.
# numbers is now [1, 10, 5, 16, 40, 9, 10]
numbers[4] = 40

# append() adds a single item to the end of the list, one call per item.
numbers.append(49)  # [1, 10, 5, 16, 40, 9, 10, 49]
numbers.append(59)  # [1, 10, 5, 16, 40, 9, 10, 49, 59]
# insert(index, value) shifts everything at/after `index` one slot to the
# right and puts `value` in the freed-up spot.
numbers.insert(3, 78)   # [1, 10, 5, 78, 16, 40, 9, 10, 49, 59]
# insert(-1, value) inserts BEFORE the last element, not after it --
# negative indices for insert() still mean "this position", and the new
# item is placed there while pushing the old occupant (and everything
# after it) one step further along.
# Result: [1, 10, 5, 78, 16, 40, 9, 10, 49, 52, 59]
numbers.insert(-1, 52)

# pop() without an argument removes and returns the LAST item; pop(index)
# removes the item at that position; remove(value) deletes the first item
# that equals value (not shown active here, but useful to know):
# numbers.pop()
# numbers.pop(0)
# numbers.pop(-1)
# numbers.remove(59)

# sort() reorders the list in place (no new list is created) in ascending
# order by default.
# Before: [1, 10, 5, 78, 16, 40, 9, 10, 49, 52, 59]
# After:  [1, 5, 9, 10, 10, 16, 40, 49, 52, 59, 78]
numbers.sort()
# reverse() simply flips the current order -- it does NOT sort descending
# on its own, it just reverses whatever order the list is already in.
# Since numbers was just sorted ascending, reversing it now gives
# descending order: [78, 59, 52, 49, 40, 16, 10, 10, 9, 5, 1]
numbers.reverse()

# letters starts as ['a', 'g', 's', 'b', 'y', 'a', 's'].
# sort() on strings compares them alphabetically:
# ['a', 'a', 'b', 'g', 's', 's', 'y']
letters.sort()
# reverse() flips that to: ['y', 's', 's', 'g', 'b', 'a', 'a']
letters.reverse()

# Note: sort() followed by reverse() gives the same result as
# sort(reverse=True), just in two steps.
print(numbers)  # [78, 59, 52, 49, 40, 16, 10, 10, 9, 5, 1]
print(letters)  # ['y', 's', 's', 'g', 'b', 'a', 'a']

# len() counts the number of items currently in the list.
print(len(numbers))  # 11
print(len(letters))  # 7

# count(value) tells you how many elements are equal to value.
print(numbers.count(10))   # 2 -- there are two 10s in numbers
print(letters.count('a'))  # 2 -- there are two 'a's in letters

# clear() empties the list in place, leaving [] behind.
numbers.clear()
print(numbers)  # []
