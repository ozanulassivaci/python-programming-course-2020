# Identity Operator: is

# x = y = [1, 2, 3]
# Chained assignment: this creates ONE list and makes both x and y point
# at that same object (not two separate lists with equal contents).
# z = [1, 2, 3]
# z is a SEPARATE list that just happens to contain the same values.

# print(x==y)
# "==" compares VALUES. True, since x and y are the same object and
# therefore obviously have equal contents too.
# print(x==z)
# True -- x and z hold equal values, even though they are different
# objects in memory.
# print(x is y)
# "is" compares IDENTITY (are these literally the same object?). True,
# because the chained assignment made x and y point at one shared list.
# print(x is z)
# False -- z is a distinct list object, even though its contents look
# identical to x's.


x = [1, 2, 3]
y = [2, 4]

# del removes an item by index. x[2] is the 3rd item (value 3), so after
# this x becomes [1, 2].
del x[2]
# Assigning to an index replaces that item: y[1] = 1 turns y from
# [2, 4] into [2, 1].
y[1] = 1
# reverse() flips the order in place: [2, 1] becomes [1, 2].
y.reverse()

# At this point x is [1, 2] and y is [1, 2] -- equal values, but they
# were built completely independently, so they are two different objects.
print(x == y)      # True  -- same values
print(x is y)       # False -- different objects in memory
print(x is not y)  # True  -- the negation of "is"; confirms they are
                    # NOT the same object


# Membership Operator: in

x = ['apple', 'banana']
# "in" checks whether a value exists as an ELEMENT of a list (matched by
# equality, not identity).
print('banana' in x)  # True

name = 'Kerem'
# For strings, "in" checks for a SUBSTRING rather than a list element.
# 'Kerem' is K-e-r-e-m -- there is no 'a' anywhere in it, so this is False.
print('a' in name)      # False
print('a' not in name)  # True -- the negation of "in"
