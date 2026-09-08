x = '10'
y = '20'

# x = y makes x point at the same string object y currently points at.
# Strings are immutable, so this is completely safe -- there's no way to
# "mutate" a string in place, so nothing you do to one variable can ever
# leak into another this way.
x = y

# Reassigning y here makes y point at a brand-new string, '5'. This does
# NOT change what x points at -- x still refers to the old '20' value.
# "=" always just re-points a name; it never edits the previous value.
y = '5'

print(x)  # '20'
print(y)  # '5'


# Contrast the above with a MUTABLE type like a list, to see why the
# distinction between "same value" and "same object" matters:

# x = ["apple", "banana"]
# y = ["apple", "banana"]
# These look identical, but they are two SEPARATE list objects that just
# happen to contain equal values.

# y = x
# Now both names point at the SAME list object in memory (no new list was
# created -- y simply refers to whatever x refers to).

# print(x is y)
# "is" checks object IDENTITY (are these literally the same object in
# memory?), not just equal values -- this differs from "==", which checks
# whether the values look the same. Since y = x made them share one
# object, this prints True.

# x[0] = 'grape'
# Because x and y point at the SAME mutable list, mutating it "through"
# x is instantly visible "through" y too -- there's only one list object,
# with two names both pointing at it.

# print(x is y)
# Still True -- mutating the shared list's contents doesn't create a new
# object, so identity is unaffected.

# print(x)
# print(y)
# Both would print ['grape', 'banana'], since they're really the exact
# same list.
