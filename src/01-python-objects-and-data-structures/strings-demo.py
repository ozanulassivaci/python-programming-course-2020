website = "http://www.ozanulassivaci.com"
course = "Python Course: Your Guide to Python Programming from Start to Finish (40 hours)"

# 1- How many characters does 'course' contain?
# len() counts every character, including spaces and punctuation.
result = len(course)
length = len(website)  # website has 29 characters (indices 0 through 28)

# 2- Grab the "www" characters out of 'website'.
# Counting from 0: h(0)t(1)t(2)p(3):(4)/(5)/(6)w(7)w(8)w(9).(10)...
# A slice a[start:stop] returns the characters from index `start` up to
# but NOT including index `stop`. website[7:10] grabs indices 7, 8, 9,
# which are exactly the three "w" characters.
result = website[7:10]

# 3- Grab the "com" characters out of 'website'.
# Continuing the index count from above: ...o(11)z(12)a(13)n(14)u(15)
# l(16)a(17)s(18)s(19)i(20)v(21)a(22)c(23)i(24).(25)c(26)o(27)m(28).
# website[22:25] actually lands on indices 22-24, which spell "aci"
# (the tail end of "ozanulassivaci"), NOT "com" -- a good example of how
# easy it is to miscount by hand when slicing. The line below fixes it
# properly by counting backward from the known length instead: index
# (length-3) is 3 characters before the end, so [length-3:length] always
# grabs exactly the last 3 characters, however long the string is.
result = website[22:25]
result = website[length-3:length]

# 4- Grab the first 15 and last 15 characters of 'course'.
result = course[0:15]   # start explicitly at 0, stop before index 15
result = course[:15]    # omitting the start defaults to 0 -- same result
result = course[-15:]   # a negative start counts from the end: "the 15th
                         # character from the end, through to the end"

# 5- Print the characters of 'course' in reverse.
# A slice's third number is the "step": how many characters to move each
# time. step = -1 with no start/stop means "walk the whole string back to
# front", which is a very common Python idiom for reversing a sequence.
result = course[::-1]

# Tuple unpacking: Python evaluates the comma-separated values on the
# right into a tuple, then matches them up positionally with the
# comma-separated names on the left, one-to-one, in a single statement.
name, surname, age, job = 'Bora', 'Yilmaz', 32, 'engineer'

# 6- Using the variables above, print the following sentence:
#    'My name is Bora Yilmaz, I am 32 years old and I work as an engineer.'

# Approach A: manual concatenation with "+". Note age is an int, so it
# must be converted with str() before it can be glued to other strings.
result = "My name is " + name + " " + surname + ", I am " + str(age) + " years old and I work as an " + job

# Approach B: the str.format() method. The curly braces {0}, {1}, {2}, {3}
# are placeholders filled in by the *position* of the arguments passed to
# format() -- {0} becomes the 1st argument (name), {1} the 2nd (surname),
# and so on. format() also converts non-string values (like age) to text
# automatically, so no manual str() call is needed here.
result = "My name is {0} {1}, I am {2} years old and I work as an {3}.".format(name, surname, age, job)

# Approach C: an f-string (formatted string literal), the letter f right
# before the opening quote. Anything inside {curly braces} is evaluated as
# a real Python expression and its result is inserted directly into the
# string. This is the most modern and usually most readable way to build
# strings with embedded values. Note: the double quotes around "I work as
# an" here are just literal characters that will show up in the output
# (Python doesn't treat them specially since the string itself uses single
# quotes as its delimiter).
result = f'My name is {name} {surname}, I am {age} years old and "I work as an" {job}.'

# 7- Replace the w in 'Hello world' with 'W'.
s = 'Hello world'
# Indices: H(0)e(1)l(2)l(3)o(4) (5)w(6)o(7)r(8)l(9)d(10)
# s[0:6]  -> "Hello " (indices 0-5, including the trailing space)
# s[-4:]  -> "orld"   (the last 4 characters)
# Since strings are immutable in Python (you can't change a character in
# place), the usual trick is to build a brand new string that reuses the
# parts you want to keep and drops in the replacement in between.
s = s[0:6] + 'W' + s[-4:]

print(s)
# 8- Print 'abc' three times in a row.
# Multiplying a string by an integer with "*" repeats it that many times
# and concatenates the copies together. 'abc ' * 3 -> 'abc abc abc '
# (the trailing space in the literal gets repeated too).
result = 'abc ' * 3

print(result)
