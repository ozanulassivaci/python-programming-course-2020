# up to 100

# x = 1
# while x <= 100:
#     if x % 2==1:
#         print(f'odd number: {x}')
#     else:
#         print(f'even number: {x}')
#     x += 1
# Standard "count up with a while loop" pattern: keep looping while the
# condition (x <= 100) holds, and manually move x forward by 1 each time
# -- printing whether each number from 1 to 100 is odd or even along the
# way (using the same "% 2" remainder trick seen throughout this course).

# print('done...')


name = ''  # False
# Tried this with just `not name.strip()` first, but isspace() reads
# cleaner for "did the user just mash the space bar".
# str.isspace() returns True only when the string is NON-EMPTY and every
# single character in it is whitespace (spaces, tabs, newlines, etc).
# Crucially, it returns False for an EMPTY string -- an empty string
# isn't "all whitespace", it's just nothing at all. That's exactly what
# the "# False" note above is flagging: ''.isspace() evaluates to False.
# Because of that, the while condition below is False from the very
# first check, so this loop's body never runs even once -- the user is
# never actually prompted here, and `name` stays '' all the way down to
# the print() call. (If `name` had instead started out holding actual
# whitespace, like ' ', the loop WOULD run and keep re-prompting until
# something other than pure whitespace was entered.)
while name.isspace():
    name = input('enter your name: ')

print(f'Hello, {name}')
