website = "http://www.ozanulassivaci.com"
course = "Python Course: Your Guide to Python Programming from Start to Finish (40 hours)"


# 1-  Strip the leading and trailing spaces from ' Hello World '.
result = ' Hello World '.strip()
result = ' Hello World '.lstrip()
result = ' Hello World '.rstrip()

result = website.lstrip('/:pth')

# 2- Strip every character from 'www.ozanulassivaci.com' except the "ozanulassivaci" part.
result = 'www.ozanulassivaci.com'.strip('w.moc')

# 3-  Turn every character in 'course' into lowercase.
result = course.lower()
result = course.upper()
result = course.title()

# 4- How many 'a' characters are in 'website'? (count('a'))
result = website.count('a')
result = website.count('www')
result = website.count('www', 0, 10)

# 5- Does 'website' start with "www" and end with "com"?
result = website.startswith('www')
result = website.startswith('http')
result = website.endswith('com')

# 6-  Does 'website' contain '.com'?
result = website.find('com')
result = website.find('com', 0, 10)
result = course.find('Python')
result = course.rfind('Python')

result = website.index('com')
result = website.rindex('com')
# result = website.rindex('comm') # exception

# 7- Are all the characters in 'course' alphabetic? (isalpha, isdigit)
result = course.isalpha()
result = 'Hello'.isalpha()
result = course.isdigit()
result = '123'.isdigit()

# 8- Center 'Contents' in a 50-character line, padded with * on both sides.
result = 'Contents'.center(50, '*')
result = 'Contents'.ljust(50, '*')
result = 'Contents'.rjust(50, '*')

# 9-  Replace every space in 'course' with '-'.
result = course.replace(' ', '-')
result = course.replace(' ', '-', 5)
result = course.replace(' ', '')

# 10- Replace 'World' with 'There' in 'Hello World'.
result = 'Hello World'.replace('World', 'There')

# 11-  Split 'course' on its space characters.
result = course.split(' ')
# result = result[2]
result = result[5]

print(result)
