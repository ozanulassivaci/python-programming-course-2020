# str.split() with no argument splits on whitespace (spaces, tabs,
# newlines) and drops the whitespace itself, returning a list of the
# remaining pieces. Punctuation attached to a word (like the period after
# "There.") stays attached -- split() only cuts on whitespace.
# Result: ['Hello', 'There.', 'My', 'name', 'is', 'Ozan', 'Ulaş']
message = 'Hello There. My name is Ozan Ulaş'.split()
# print(message[0])

# A list can hold items of a single type...
# my_list = [1,2,3]
# ...or freely mix different types in one list -- string, int, bool, float.
# my_list = ['one', 2, True, 5.6]
# print(my_list)

list1 = ['one', 'two', 'there']
list2 = ['four', 'five', 'six']

# "+" between two lists concatenates them into a new list (it does not
# modify list1 or list2): ['one','two','there','four','five','six']
numbers = list1 + list2
print(numbers)
print(len(numbers))    # 6 total items
print(message[0])      # 'Hello' -- first word from the split above
print(numbers[2])      # 'there' -- 3rd item (index 2) of the merged list

userA = ['Ozan', 36]
userB = ['Kerem', 2]

# Lists can contain other lists as elements -- here `users` is a list of
# two-item lists, effectively a tiny table of [name, age] rows.
users = [userA, userB]

print(userA)
print(userB)
print(users)

# users[0] is userA (['Ozan', 36]); indexing again with [0] reaches its
# first element, the string 'Ozan'. Chaining [i][j] like this steps one
# level deeper into a nested list each time.
print(users[0][0])
