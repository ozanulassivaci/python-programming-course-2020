numbers = []
# range(10) produces the integers 0, 1, 2, ..., 9 (10 numbers, starting at
# 0 and stopping BEFORE 10) -- a very common way to "loop N times" or
# generate a sequence of consecutive numbers.
for x in range(10):
    numbers.append(x)

print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# A "list comprehension" builds the exact same list in a single, compact
# expression: [<expression> for <item> in <sequence>]. Python runs the
# loop internally and collects every <expression> result into a new list.
# This line produces an identical result to the 3-line loop above.
numbers = [x for x in range(10)]
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in range(10):
    print(x**2)  # prints 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, one per line

# The <expression> part of a comprehension can be anything, not just the
# bare loop variable -- here it's x**2 (x squared), so each collected
# value is the square of the corresponding x from range(10).
numbers = [x**2 for x in range(10)]
print(numbers)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# A comprehension can also include an "if" clause at the end, which acts
# as a FILTER: only items for which the condition is True get included at
# all (this is different from the if/else form further down, which
# always includes every item but chooses what value to use).
# range(10) is 0..9; keeping only x % 3 == 0 leaves 0, 3, 6, 9, and each
# of those gets squared (x*x): 0, 9, 36, 81.
numbers = [x*x for x in range(10) if x % 3 == 0]
print(numbers)  # [0, 9, 36, 81]

my_string = 'Hello'
my_list = []

for letter in my_string:
    my_list.append(letter)
print(my_list)  # ['H', 'e', 'l', 'l', 'o']

# Same result as the loop above, just as a one-liner
my_list = [letter for letter in my_string]
print(my_list)  # ['H', 'e', 'l', 'l', 'o']

years = [1983, 1999, 2008, 1956, 1986]
# The expression can reference each item however you like -- here it
# computes an age from each birth year. Result, year by year:
# 2019-1983=36, 2019-1999=20, 2019-2008=11, 2019-1956=63, 2019-1986=33
ages = [2019-year for year in years]
print(ages)  # [36, 20, 11, 63, 33]

# This is the "conditional expression" form: `A if <condition> else B`.
# Unlike the filtering "if" used earlier, this does NOT drop any items --
# every x from range(1, 10) (1 through 9) is included, but the VALUE
# stored for each one depends on the condition: even numbers keep their
# numeric value (x), while odd numbers are replaced with the string
# 'ODD'. So the results list ends up with a deliberate mix of ints and
# strings.
results = [x if x % 2 == 0 else 'ODD' for x in range(1, 10)]
print(results)  # ['ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD']

result = []

# A nested for loop (a loop inside another loop): for every value of x,
# the ENTIRE inner loop over y runs from start to finish before x moves
# to its next value. This produces every possible (x, y) pairing between
# the two ranges -- 3 x-values times 3 y-values = 9 tuples total.
for x in range(3):
    for y in range(3):
        result.append((x, y))

print(result)
# [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

# List comprehensions support multiple "for" clauses too, which behave
# exactly like nested loops written left to right (the leftmost `for` is
# the outermost loop). This one has three ranges of 3 values each, so it
# produces 3*3*3 = 27 (x, y, z) tuples covering every combination.
numbers = [(x, y, z) for x in range(3) for y in range(3) for z in range(3)]
print(numbers)
