# def square(num): return num ** 2
# A lambda is a small, unnamed ("anonymous") function written as a single
# expression: `lambda <parameters>: <expression>`. It's equivalent to
# defining a normal function with `def` and a `return`, just in a more
# compact form -- useful when you need a quick, throwaway function
# (often passed straight into another function) without giving it a
# whole `def` block.
# square =  lambda num: num ** 2

numbers = [1, 3, 5, 9, 10, 4]

# map(function, sequence) applies `function` to every item in `sequence`
# and gives back an iterator of the results. Like range() and zip(), it's
# lazy, so list(...) is needed to see all the results at once.
# result = list(map(lambda num: num ** 2, numbers))  # squares every number
# result = list(map(square, numbers))                 # same, using the named lambda above
# result = square(3)                                  # calling it directly: 9

# for item in map(square, numbers):
#     print(item)
# Looping directly over the map object avoids materializing the whole
# list at once -- each squared value is produced just in time as the
# loop asks for it.

# def check_even(num): return num%2==0
# Same idea as `square` above: a lambda that checks whether a number is
# even, stored under a name so it can be reused like a regular function.
check_even = lambda num: num % 2 == 0

# filter(function, sequence) keeps only the items for which `function`
# returns True, discarding the rest -- again lazy, so list(...) forces it
# to actually run and collect the results.
# result = list(filter(check_even, numbers))                  # [10, 4] -- the even numbers
# result = list(filter(lambda num: num%2==0, numbers))         # same, with an inline lambda
# result = list(filter(check_even, numbers))

# numbers = [1, 3, 5, 9, 10, 4]; numbers[2] is the 3rd element, 5.
# check_even(5) -> 5 % 2 == 0 -> False (5 is odd).
result = check_even(numbers[2])


print(result)  # False
