# GENERATORS
#
# A generator is a special, easy way to build an iterator (see 11-iterators
# for what an iterator is) without writing a class with __iter__/__next__ by
# hand. Python builds the iterator machinery for you automatically whenever
# a function uses the "yield" keyword, or whenever you write a "generator
# expression" like the one below.

# def cube():
#     for i in range(5):
#         # "yield" is like "return", except the function doesn't end here.
#         # It pauses, hands the value out to whoever is iterating, and then
#         # picks up again - right after this line, with all its local
#         # variables (like i) exactly as they were - the next time a value
#         # is requested. A function containing "yield" becomes a "generator
#         # function": calling cube() doesn't run any of this code yet, it
#         # just creates a generator object ready to run it on demand.
#         yield i ** 3

# for i in cube():
#     print(i)
# This for-loop would print 0, 1, 8, 27, 64 - i.e. i**3 for i = 0..4 - but
# crucially, cube() never builds a list like [0, 1, 8, 27, 64] in memory.
# Each cubed value is computed and yielded one at a time, only when the
# for-loop asks for the next one. That's the main advantage of generators
# over building and returning a full list: they use very little memory,
# which matters a lot when the sequence is huge (or infinite).

# This is the first time I used a generator expression instead of building a whole list in memory.
# The syntax "(expression for item in iterable)" - round parentheses - looks
# almost identical to a list comprehension "[expression for item in iterable]"
# with square brackets, but it behaves completely differently:
#   - [i**3 for i in range(5)] immediately computes ALL 5 cubes and stores
#     them in a real list in memory: [0, 1, 8, 27, 64].
#   - (i**3 for i in range(5)) creates a generator object instead. No cubes
#     have been computed yet - it's essentially a paused recipe for
#     producing them one at a time, exactly like the yield-based cube()
#     function above, just written in a single compact expression.
generator = (i**3 for i in range(5))

# Printing the generator itself does NOT print its values - it prints
# something like "<generator object <genexpr> at 0x...>", because at this
# point nothing has been computed or consumed yet; the generator is just an
# object sitting there, ready to be iterated.
print(generator)

# Iterating with a for-loop calls next() on the generator behind the scenes,
# over and over, until it raises StopIteration - each call computes exactly
# one more value (0, then 1, then 8, then 27, then 64) instead of all five
# up front. This prints each cube on its own line.
for i in generator:
    print(i)

# print(next(generator))
# print(next(generator))
# print(next(generator))
# Note: a generator can only be consumed once. After the for-loop above has
# already pulled every value out of "generator" (exhausting it), calling
# next(generator) again here would immediately raise StopIteration instead
# of restarting from 0 - you'd need to create a brand new generator
# expression to iterate over the same cubes again.
