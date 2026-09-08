# x = int(input('x: '))
# y = int(input('y: '))

# An if/elif/else chain tests conditions from top to bottom and runs the
# code under the FIRST one that turns out True, skipping all the rest --
# even if a later condition would also have been True.
# if x > y:
#     print('x is greater than y')
# elif x == y:
#     print('x equals y')
# else:
#     print('y is greater than x')


num = int(input('number: '))

# Indentation (the 4 spaces before each print) is what defines the block
# of code that belongs to each branch -- Python uses indentation itself
# as the syntax for grouping statements, instead of curly braces {} like
# many other languages.
if num > 0:
    print('the number is positive')
# elif ("else if") lets you check another condition only when the ones
# above it were False. Python only reaches this line if `num > 0` was False.
elif num < 0:
    print('the number is negative')
# else is the catch-all: it runs only if NONE of the conditions above it
# were True. Here that means num is neither greater than 0 nor less than
# 0, so it must be exactly 0.
else:
    print('the number is zero')
