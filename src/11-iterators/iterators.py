# ITERATORS
#
# An "iterable" is anything you can loop over with a for-loop (lists, tuples,
# strings, dicts, sets, files, ...). Under the hood, a for-loop doesn't
# actually know how to walk through each of those data types directly -
# instead, it asks the iterable to hand it an "iterator" object, and then it
# repeatedly asks that iterator for "the next value" until there are none
# left. This file explores that machinery directly, without a for-loop
# hiding it from us.

# numbers = [1,2,3,4,5]

# iter(x) converts an iterable (here, a list) into an iterator. The iterator
# remembers "where we are" in the sequence - the list itself does not.
# iterator = iter(numbers)

# next(x) asks the iterator for the next value and advances its internal
# position by one. Calling it 5 times here returns 1, 2, 3, 4, 5 in order -
# one value consumed per call.
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# # Calling next() a 6th time (after all 5 values are used up) would raise a
# # StopIteration exception - that's how Python signals "there's nothing left".
# # print(next(iterator))

# for i in numbers:
#     print(i)
# The loop above does exactly what the manual iter()/next() calls do below,
# just automatically: it calls iter(numbers) once to get an iterator, then
# calls next() on it over and over, and stops cleanly (without crashing your
# program) the moment it catches a StopIteration.

# numbers = [1,2,3,4,5]
# iterator = iter(numbers)

# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         # This is precisely what a for-loop does behind the scenes: keep
#         # calling next() until it fails with StopIteration, then stop
#         # looping instead of letting the exception crash the program.
#         break

# Building my own iterable by defining __iter__ and __next__ instead of using a builtin.
# This is called the "iterator protocol": any object that implements both
# __iter__ (returns an iterator - often just "self") and __next__ (returns
# the next value, or raises StopIteration when done) can be used anywhere
# Python expects an iterator, including in a for-loop or with next().
class MyNumbers:
    def __init__(self, start, stop):
        # These two attributes are the object's "state": start is the next
        # value we're about to hand out, and stop is the last value we'll
        # ever return before we run out.
        self.start = start
        self.stop = stop

    def __iter__(self):
        # iter(some_instance) calls this method. Because MyNumbers already
        # keeps its own position (self.start) and knows how to produce the
        # next value, the object can act as its own iterator - so it simply
        # returns itself instead of building a separate iterator object.
        return self

    def __next__(self):
        # next(some_instance) calls this method. Each call must either
        # return the next value or raise StopIteration - there's no other
        # way for a caller to know the sequence has ended.
        if self.start <= self.stop:
            x = self.start
            self.start += 1  # advance our internal position for next time
            return x
        else:
            # We've already returned every number from the original start
            # up to stop, so there's nothing left to give out.
            raise StopIteration

# Creates one MyNumbers object that will eventually produce 20, 21, 22, ..., 50.
# Nothing has been iterated yet at this point - the numbers are generated lazily,
# one at a time, only when something calls next() on it.
number_range = MyNumbers(20,50)

# Since MyNumbers.__iter__ just returns self, calling iter() on it here is
# technically redundant (myiter and number_range end up being the very same
# object) - but writing it this way mirrors how you'd normally get an
# iterator from any iterable, custom or built-in.
myiter = iter(number_range)

# print(next(myiter))
# print(next(myiter))

# Manually driving the iterator: keep asking for the next value and print it,
# until __next__ raises StopIteration, at which point we break out of the
# infinite loop instead of letting the program crash.
while True:
    try:
        element = next(myiter)
        print(element)
    except StopIteration:
        break


# for x in number_range:
#     print(x)
# Careful: because __next__ mutates self.start in place, once the while-loop
# above has already consumed every value (start has climbed past stop), a
# fresh "for x in number_range" here would find self.start already greater
# than self.stop and immediately hit StopIteration - printing nothing. A
# single MyNumbers instance can only be iterated through once; to loop over
# 20-50 again you'd need to create a brand new MyNumbers(20, 50) object.
