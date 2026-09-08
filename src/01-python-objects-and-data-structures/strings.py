name = 'Ozan'
surname = 'Sıvacı'
age = 36

# str(age) converts the integer 36 into the text "36" so it can be joined
# with "+" to other strings -- you cannot "+" a string and an int directly
# (that raises a TypeError), because Python refuses to guess whether you
# meant addition or concatenation.
# '\n' inside the string is an escape sequence: two characters (backslash
# and n) that Python interprets as a single "newline" character, moving
# whatever comes after it onto a new line when printed.
greeting = 'My name is ' + name + ' ' + surname + ' and \nI am ' + str(age) + ' years old'

# len() is a built-in function that returns how many characters are in a
# string (or how many items are in other sequences, like lists).
length = len(greeting)

# Strings support "indexing" with square brackets: greeting[i] gives you
# the single character at position i. Indexing starts at 0, so index 0 is
# the very first character.
# print(greeting)
# print(greeting[0])          # the 1st character
# print(greeting[3])          # the 4th character
# print(greeting[length-1])   # the last character (since indices run
#                              # from 0 to length-1)
# print(greeting[-1])         # negative indices count from the end, so -1
#                              # is a shortcut for "the last character"
#                              # without needing to know the string's length

# "Slicing" lets you pull out a whole sub-string with start:stop, meaning
# "from index start up to (but NOT including) index stop".
# print(greeting[3:7])   # characters at indices 3, 4, 5, 6
# print(greeting[3:])    # from index 3 to the end (omitting stop means "to the end")
# print(greeting[:16])   # from the start up to (not including) index 16

# A slice can also take a third number: start:stop:step, where step is
# how many characters to advance each time. Here step is 3, so we take
# the character at index 2, then 5, then 8, then 11, ... up to (not
# including) index 40, skipping two characters between each pick.
print(greeting[2:40:3])
