x = 5

attempts_left = 0
keep_going = 'y'

result = 5 < x < 10

# and

# True, True => True
# True, False => False


result = (x > 5) and (x < 10)
result = (attempts_left > 0) and (keep_going == 'y')

# or

result = (x > 0) or (x % 2 == 0)

# True, False => True
# True, True => True
# False, False => False

# not

result = not (x > 0)

# is x an even number between 5 and 10?

result = ((x > 5) and (x < 10)) and (x % 2 == 0)

print(result)
