# range
# range(start, stop, step) generates numbers from start up to (but not
# including) stop, advancing by step each time. range(50,100,20) would
# give 50, 70, 90 (the next one, 110, would be >= 100, so it stops there).
# for item in range(50,100,20):
#     print(item)

# range() itself is a special lazy sequence, not a list -- wrapping it in
# list(...) forces it to produce an actual list you can print or inspect
# directly. range(5,100,10) counts 5, 15, 25, ..., 95 (stopping before 100).
# print(list(range(5,100,10)))

# enumerate
# enumerate(sequence) wraps any sequence so that looping over it gives you
# BOTH the index and the item together, as (index, item) pairs, without
# having to maintain a separate counter variable yourself.

# greeting = 'Hello'

# for index, item in enumerate(greeting):
#     print(f'index: {index} letter: {item}')
# Would print: index 0 letter H, index 1 letter e, index 2 letter l,
# index 3 letter l, index 4 letter o.

# zip

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = [100, 200, 300, 400, 500]

# zip(a, b, c, ...) pairs up items from multiple sequences by POSITION:
# the 1st items from each become one tuple, the 2nd items become the
# next tuple, and so on. Like range(), zip() is lazy, so wrapping it in
# list(...) is needed to see (or print) all the pairs at once.
# Result: [(1,'a',100), (2,'b',200), (3,'c',300), (4,'d',400), (5,'e',500)]
print(list(zip(list1, list2, list3)))

# Looping directly over a zip object gives you one combined tuple per
# iteration, without needing to wrap it in list() first.
for item in zip(list1, list2, list3):
    print(item)

# And just like with the list-of-tuples example in for.py, each tuple
# produced by zip can be unpacked straight into separate loop variables.
for a, b, c in zip(list1, list2, list3):
    print(a, b, c)
