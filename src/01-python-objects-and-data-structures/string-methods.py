message = 'Hello There. My name is Ozan Ulaş'
# split() with no argument breaks the string on whitespace, discarding it,
# and returns a LIST of the words. After this line, message is no longer
# a string -- it's ['Hello', 'There.', 'My', 'name', 'is', 'Ozan', 'Ulaş'].
message = message.split()


# All of the lines below assume message is still a STRING, so if you
# uncommented them now they would fail with an AttributeError (lists
# don't have string methods like .upper() or .split()) -- they're really
# meant to be tried one at a time, starting over from the original
# `message = 'Hello There. My name is Ozan Ulaş'` string each time.

# message = message.upper()       # every letter uppercase
# message = message.lower()       # every letter lowercase
# message = message.title()       # Every Word Capitalized
# message = message.capitalize()  # only the very first letter capitalized,
                                   # the rest lowercased

# message = message.strip()       # remove leading/trailing whitespace
# message = message.split()       # split on whitespace into a list of words
# message = message.split('.')    # split on the '.' character specifically
# join() is the mirror image of split(): it glues a list of strings back
# together, inserting the string it's called on between every pair of
# items. '---'.join(['a','b','c']) would give 'a---b---c'.
# message = '---'.join(message)

# index = message.find('Ozan')       # position of the first match, or -1
# is_found = message.startswith('H')  # True/False
# is_found = message.endswith('n')    # True/False

# message = message.replace('Ozan','Kerem')  # swap all occurrences
# You can chain multiple .replace() calls one after another, since each
# call returns a new string that the next .replace() can be called on --
# just make sure each call after the first starts on the SAME line or is
# wrapped in parentheses, since Python doesn't allow a bare line break
# here without one.
# message = message.replace('c','c')
#                  .replace('o','o')
#                  .replace(' ','-')

# Because message is currently a LIST (from split() above, not a string),
# calling a string-only method like center() on it raises an
# AttributeError: 'list' object has no attribute 'center' -- this line
# will crash the script when run. It's a good reminder to keep track of
# what type a variable currently holds, especially after reassigning it
# partway through a script.
message = message.center(50, '*')

print(message)
