# value types => string, number
# Numbers (and strings) are immutable: there is no operation that changes
# the number 5 itself, only ways to make a name point at a different value.
x = 5
y = 25

# x = y makes x point at the same value y currently holds (25).
x = y

# Reassigning y afterwards only changes what y points at -- it has no
# effect on x, which keeps pointing at 25. Each variable is an independent
# pointer to a value; "=" never links two names together permanently.
y = 10

# print(x,y)
# Would print: 25 10

# reference types => list
# Learned the hard way that lists are reference types: reassigning
# `a = b` makes both names point at the same list, so mutating one
# through `b[0] = ...` shows up when you print `a` too.
a = ["apple", "banana"]
b = ["apple", "banana"]

# Before this line, a and b are two DIFFERENT list objects that happen to
# have equal contents. After it, a is repointed to the SAME object as b
# -- the original list a used to point at is abandoned.
a = b

# Since a and b now refer to the one shared list, mutating it through
# either name is visible through both. This replaces index 0 of that
# shared list with "grape".
b[0] = "grape"

# Both names see the same, single, mutated list:
print(a, b)  # ['grape', 'banana'] ['grape', 'banana']
