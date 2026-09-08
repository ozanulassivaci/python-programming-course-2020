# "import random" pulls in Python's built-in "random" module: a
# collection of functions for generating pseudo-random numbers and
# making random choices. After importing, you access everything it
# provides with the dot syntax random.<name>, so it doesn't clash with
# names you define yourself in this file.
import random

# result = dir(random)
# dir() lists the names (functions, constants, etc.) defined inside a
# module or object -- handy for discovering what's available.
# result = help(random)
# help() prints the module's documentation (built from its docstrings),
# describing what each function does and what arguments it takes.

# random.random() returns a random float that is always
# >= 0.0 and < 1.0 (it can equal 0.0, but never reach exactly 1.0).
result = random.random()  # 0.0 - 1.0
# Multiplying by 100 stretches that same 0.0-1.0 range into a random
# float that is >= 0.0 and < 100.0.
result = random.random() * 100
# random.uniform(a, b) directly returns a random float between a and b
# (inclusive of a, and b is possible too, unlike random()). Wrapping it
# in int() truncates the decimal part, giving a whole number that will
# be somewhere from 10 up to (at most) 99, since int() always rounds
# toward zero and 100 itself is only reachable in the vanishingly rare
# case uniform() returns exactly 100.0.
result = int(random.uniform(10, 100))
# random.randint(a, b) returns a random INTEGER, and unlike random()/
# uniform(), both endpoints are inclusive -- so this can return anything
# from 1 to 100, including 1 and 100 themselves.
result = random.randint(1, 100)

greeting = 'hello there'
names = ['ali', 'yagmur', 'deniz', 'cenk', 'ahmet', 'efe']
# result = names[random.randint(0,len(names)-1)]
# This commented-out line shows the "manual" way to pick a random
# element from a list before you know about random.choice(): pick a
# random valid index (0 through len(names)-1) and index into the list
# with it. random.choice() below does the same job more directly.

# random.choice(sequence) picks and returns one random element from any
# sequence (list, string, tuple, ...) -- here, one random name from the
# list.
result = random.choice(names)
# Since a string is also a sequence of characters, random.choice() works
# on it too: this returns one random single character from
# 'hello there' (which could even be the space character).
result = random.choice(greeting)

# Learned that shuffle() reorders a list in place and returns None.
# random.shuffle(list) does NOT return a new shuffled list -- it
# rearranges the elements of the list you pass in directly (mutates it
# "in place") and gives back None. That's why the code below assigns
# `numbers` first, calls shuffle() as its own statement (ignoring any
# return value), and only afterwards reads `numbers` again to see the
# shuffled order.
numbers = list(range(10))  # numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(numbers)
result = numbers  # same 10 numbers as before, just reordered randomly

# range(100) lazily represents the integers 0 through 99 without
# building a full list in memory up front.
numbers = range(100)
# random.sample(population, k) returns a NEW list containing k unique
# elements chosen at random from population, without ever picking the
# same element twice (unlike random.choice() called repeatedly, which
# could repeat elements). Here it picks 3 distinct numbers from 0-99.
result = random.sample(numbers, 3)
# And here it picks 2 distinct names from the `names` list -- never the
# same name twice in one result.
result = random.sample(names, 2)

print(result)
