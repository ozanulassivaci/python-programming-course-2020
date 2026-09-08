# 1-  Create a list with elements "Bmw, Mercedes, Opel, Mazda".
# A list is an ordered, mutable collection, written with square brackets
# and comma-separated values. "Ordered" means items keep the position you
# put them in; "mutable" means you can change, add, or remove items after
# creating it (unlike a string or tuple).
cars = ['Bmw', 'Mercedes', 'Opel', 'Mazda']
# 2-  How many elements does the list have?
result = len(cars)  # 4
# 3-  What are the first and last elements of the list?
result = cars[0]   # 'Bmw'        (index 0 = first item)
result = cars[3]   # 'Mazda'      (index 3 = 4th item, the last one here)
result = cars[-1]  # 'Mazda'      (-1 always means "the last item",
                    #              regardless of the list's length)
# 4-  Replace Mazda with Toyota.
# Assigning to an index replaces just that one element.
# cars[-1] = 'Toyota'
result = cars
# 5-  Is Mercedes an element of the list?
# The "in" operator scans the list and returns True/False.
result = 'Mercedes' in cars  # True
# 6-  What is the value at index -2?
# Negative indices count backwards: -1 is the last item, -2 is the
# second-to-last, and so on. cars is ['Bmw','Mercedes','Opel','Mazda'],
# so -2 lands on 'Opel'.
result = cars[-2]
# 7-  Get the first 3 elements of the list.
result = cars[0:3]  # ['Bmw', 'Mercedes', 'Opel']
result = cars[:3]   # same thing -- an omitted start defaults to 0
result = cars[-2:]  # ['Opel', 'Mazda'] -- from the 2nd-to-last to the end
# 8-  Replace the last 2 elements with "Toyota" and "Renault".
# You can assign to a SLICE, not just a single index, to replace several
# items at once. This overwrites the last two elements ('Opel', 'Mazda')
# with the two new values, so cars becomes:
# ['Bmw', 'Mercedes', 'Toyota', 'Renault']
cars[-2:] = ['Toyota', 'Renault']
result = cars
# 9-  Append "Audi" and "Nissan" to the list.
# "+" between two lists concatenates them into a brand-new list; it does
# NOT modify cars in place (that's what append()/extend() are for).
result = cars + ['Audi', 'Nissan']
# 10- Remove the last element of the list.
# del removes an item (or a slice) by index/position, in place.
# cars becomes ['Bmw', 'Mercedes', 'Toyota'] (dropping 'Renault').
del cars[-1]
result = cars
# 11- Print the list elements in reverse.
# Same reversing trick as with strings: a full slice with step -1.
result = cars[::-1]  # ['Toyota', 'Mercedes', 'Bmw']
# 12- Store the following data in a list.

      # studentA: Yigit Bilgi 2010, (70,60,70)
      # studentB: Sena Oznur  1999, (80,80,70)
      # studentC: Ahmet Aykut 1998, (80,70,90)

# Lists can hold items of different types, including other lists --
# here each student is [first_name, last_name, birth_year, [grades]],
# mixing strings, an int, and a nested list of ints in one structure.
studentA = ['Yigit', 'Bilgi', 2010, [70, 60, 70]]
studentB = ['Sena', 'Oznur', 1999, [80, 80, 70]]
studentC = ['Ahmet', 'Aykut', 1998, [80, 70, 90]]

# 13- Print the list elements.

result = studentA[0]  # 'Yigit'  (first name)
result = studentB[1]  # 'Oznur'  (last name)
# studentA[3][1] because the grades themselves are a list nested inside the list
# studentC[3] is the grades list [80, 70, 90]; indexing that again with
# [1] reaches its 2nd element, 70. Chaining indices like this ([3][1]) is
# how you drill into nested data structures.
result = studentC[3][1]

# f-strings can contain arbitrary expressions, including arithmetic:
# 2019 - studentA[2]  ->  2019 - 2010 = 9  (age)
# (70+60+70)/3         ->  200/3 = 66.666... (grade average; "/" always
#                          produces a float in Python 3, even when the
#                          numbers divide evenly)
result = f"{studentA[0]} {studentA[1]} is {2019-studentA[2]} years old with a grade average of {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"

print(result)
