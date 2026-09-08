
# method
# A "method" is a function that belongs to an object and is called using
# dot syntax: object.method(...). It usually acts on (or reads from) the
# object it's called on, which is why list.append(...) can add to THIS
# particular list without needing to be told which list to use -- that's
# implied by writing it as list.append(...) rather than append(list, ...).

list = [1, 2, 3]

list.append(4)  # list becomes [1, 2, 3, 4]
list.pop()      # removes and returns the last item (4); list becomes [1, 2, 3]

print(type(list))  # <class 'list'>
print(list)         # [1, 2, 3]

my_string = 'Hello'

# upper() is a method on strings -- but unlike list.append()/pop(), it
# does NOT modify my_string in place (strings can't be mutated at all).
# It returns a brand-new uppercase string, which is printed here directly
# without being stored anywhere.
print(my_string.upper())  # HELLO


print(type(my_string))  # <class 'str'> -- my_string itself is unchanged

# function
# A plain "function" (like print(), len(), or help()) isn't attached to
# any particular object -- you call it by itself, passing in whatever it
# needs to work with as arguments: e.g. len(my_string) instead of
# my_string.len(). Whether something is a function or a method just
# depends on how it's designed to be called, but both are just callable
# pieces of reusable code underneath.
