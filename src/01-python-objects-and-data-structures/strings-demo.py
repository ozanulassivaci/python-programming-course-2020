website = "http://www.ozanulassivaci.com"
course = "Python Course: Your Guide to Python Programming from Start to Finish (40 hours)"

# 1- How many characters does 'course' contain?
result = len(course)
length = len(website)

# 2- Grab the "www" characters out of 'website'.
result = website[7:10]

# 3- Grab the "com" characters out of 'website'.
result = website[22:25]
result = website[length-3:length]

# 4- Grab the first 15 and last 15 characters of 'course'.
result = course[0:15]
result = course[:15]
result = course[-15:]

# 5- Print the characters of 'course' in reverse.
result = course[::-1]

name, surname, age, job = 'Bora', 'Yilmaz', 32, 'engineer'

# 6- Using the variables above, print the following sentence:
#    'My name is Bora Yilmaz, I am 32 years old and I work as an engineer.'

result = "My name is " + name + " " + surname + ", I am " + str(age) + " years old and I work as an " + job
result = "My name is {0} {1}, I am {2} years old and I work as an {3}.".format(name, surname, age, job)
result = f'My name is {name} {surname}, I am {age} years old and "I work as an" {job}.'

# 7- Replace the w in 'Hello world' with 'W'.
s = 'Hello world'
s = s[0:6] + 'W' + s[-4:]

print(s)
# 8- Print 'abc' three times in a row.
result = 'abc ' * 3

print(result)
