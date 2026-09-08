website = "http://www.ozanulassivaci.technology"
course = "Python Course: Your Guide to Python Programming from Start to Finish (40 hours)"


# 1-  Strip the leading and trailing spaces from ' Hello World '.
# strip() removes whitespace from BOTH ends of the string by default.
result = ' Hello World '.strip()   # 'Hello World'
result = ' Hello World '.lstrip()  # 'Hello World ' -- only the left side
result = ' Hello World '.rstrip()  # ' Hello World' -- only the right side

# lstrip(chars) takes this a step further: instead of stripping
# whitespace, it strips any characters that appear in the given string,
# treating it as a SET of characters, not as a literal prefix. It removes
# characters from the left one at a time as long as they belong to that
# set, and stops at the first character that doesn't.
# Here the set is {'/', ':', 'p', 't', 'h'}. Walking website from the
# left: 'h','t','t','p',':','/','/' are all in the set and get stripped,
# then 'w' is NOT in the set, so stripping stops there.
# Result: "www.ozanulassivaci.technology"
result = website.lstrip('/:pth')

# 2- Strip every character from 'www.ozanulassivaci.com' except the "ozanulassivaci" part.
# strip(chars) again treats its argument as a set of characters to peel
# off both ends, not as a substring to protect. The set here is
# {'w', '.', 'm', 'o', 'c'}. From the left: 'w','w','w','.' get stripped,
# and then 'o' is ALSO in the set, so it gets stripped too (even though
# the intent was to keep it!) -- stripping only stops at 'z', which isn't
# in the set. From the right: 'm','o','c','.' get stripped, stopping at
# 'i'. So the actual result is "zanulassivaci", missing its leading 'o' --
# a classic strip() gotcha: it has no idea "ozanulassivaci" is a word to
# preserve, it just keeps chewing through any of the listed characters.
result = 'www.ozanulassivaci.com'.strip('w.moc')

# 3-  Turn every character in 'course' into lowercase.
result = course.lower()  # every letter lowercase
result = course.upper()  # every letter UPPERCASE
result = course.title()  # First Letter Of Each Word Capitalized

# 4- How many 'a' characters are in 'website'? (count('a'))
# count(sub) counts non-overlapping occurrences of a substring.
result = website.count('a')          # 3 -- the three 'a's inside "ozanulassivaci"
result = website.count('www')        # 1 -- "www" occurs once
# A start/end pair restricts the search to that slice of the string first
# (like website[0:10]), then counts within just that piece.
result = website.count('www', 0, 10)  # still 1, "www" fits inside the first 10 characters

# 5- Does 'website' start with "www" and end with "com"?
result = website.startswith('www')  # False -- it starts with "http", not "www"
result = website.startswith('http')  # True
# This website value ends in ".technology", not ".com", so this is False
# here (a good reminder to always check the *actual* value you're testing
# against, not just what a similar-looking example elsewhere might do).
result = website.endswith('com')

# 6-  Does 'website' contain '.com'?
# find(sub) returns the index of the first match, or -1 if not found --
# it never raises an error, which makes it safe to use for a simple
# "does this exist" check.
result = website.find('com')          # -1, because "com" isn't in this website string
result = website.find('com', 0, 10)   # also -1, restricted to website[0:10]
result = course.find('Python')        # 0 -- "Python" is the very first word
result = course.rfind('Python')       # rfind searches from the right instead,
                                       # returning the LAST occurrence's index
                                       # (the second "Python", further into
                                       # the sentence)

# index(sub) does the same job as find(), EXCEPT that when the substring
# isn't present it raises a ValueError instead of quietly returning -1.
# Since this website value does not contain "com" anywhere, this line
# actually raises an exception and would stop the script right here if
# it were run -- a very concrete illustration of why find() and index()
# are not interchangeable: pick find() when "not found" is a normal,
# expected outcome, and index() only when you're confident the substring
# must be there.
result = website.index('com')
result = website.rindex('com')
# result = website.rindex('comm') # exception -- left commented out on
# purpose, since 'comm' isn't in website either and this would also raise
# a ValueError.

# 7- Are all the characters in 'course' alphabetic? (isalpha, isdigit)
# isalpha() is True only if EVERY character is a letter and there's at
# least one character -- spaces, digits, punctuation, or an empty string
# all make it False.
result = course.isalpha()   # False -- course has spaces, ':', digits, '()'
result = 'Hello'.isalpha()  # True -- only letters
result = course.isdigit()   # False -- course has plenty of non-digit characters
result = '123'.isdigit()    # True -- every character is a digit

# 8- Center 'Contents' in a 50-character line, padded with * on both sides.
# center(width, fillchar) pads the string on both sides with fillchar
# until the total length is `width`. 'Contents' is 8 characters, so
# 50 - 8 = 42 padding characters are split evenly, 21 on each side.
result = 'Contents'.center(50, '*')
# ljust(width, fillchar) left-justifies: the original text stays on the
# left, and all the padding goes on the right.
result = 'Contents'.ljust(50, '*')
# rjust(width, fillchar) right-justifies: all the padding goes on the left.
result = 'Contents'.rjust(50, '*')

# 9-  Replace every space in 'course' with '-'.
# replace(old, new) swaps every occurrence of old for new.
result = course.replace(' ', '-')
# A 3rd argument caps how many occurrences get replaced, counting from
# the left -- here only the first 5 spaces become '-', the rest stay as
# spaces.
result = course.replace(' ', '-', 5)
# Replacing with an empty string effectively deletes every match.
result = course.replace(' ', '')

# 10- Replace 'World' with 'There' in 'Hello World'.
result = 'Hello World'.replace('World', 'There')  # 'Hello There'

# 11-  Split 'course' on its space characters.
# split(' ') breaks the string into a list wherever a space occurs.
result = course.split(' ')
# result = result[2]
# course.split(' ') gives (by position):
# 0:'Python' 1:'Course:' 2:'Your' 3:'Guide' 4:'to' 5:'Python' 6:'Programming' ...
# so index 5 is the SECOND occurrence of the word "Python".
result = result[5]

print(result)
