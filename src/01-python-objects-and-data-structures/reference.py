# value types => string, number
x = 5
y = 25

x = y

y = 10

# print(x,y)

# reference types => list
# Learned the hard way that lists are reference types: reassigning
# `a = b` makes both names point at the same list, so mutating one
# through `b[0] = ...` shows up when you print `a` too.
a = ["apple", "banana"]
b = ["apple", "banana"]

a = b

b[0] = "grape"

print(a, b)
