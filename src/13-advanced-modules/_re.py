import re

# result = dir(re)

# re module

# Regex looked like magic symbols to me at first - these notes are how I made sense of it.
text = "Python Course: Your Python Programming Guide | 40 hours"

# re.findall()

# result = re.findall("Python",text)
# result = len(result)

# re.split()

# result = re.split(" ", text)
# result = re.split("R", text)

# re.sub()

# result = re.sub(" ","-",text)
# result = re.sub("\s","-",text)

# re.search()

# result = re.search("Python",text)

# result = result.span()
# result = result.start()
# result = result.end()
# result = result.group()
# result = result.string

# regular expression

"""

    [] - Matches any single character listed inside the square brackets.

         [abc] => a      : 1 match
                  ac     : 2 match
                  Python : No matches

         [a-e]  => [abcde]
         [1-5]  => [12345]
         [0-39] => [01239]

         [^abc] => any character except a, b, or c.
         [^0-9] => any character that is not a digit.

"""

result = re.findall("[abc]",text)
result = re.findall("[sat]",text)
result = re.findall("[a-e]", text)
result = re.findall("[a-z]", text)
result = re.findall("[0-5]", text)
result = re.findall("[^abc]", text)
result = re.findall("[^0-9]", text)

"""
    . - Matches any single character.

        .. => a    : No match
              ab   : 1 match
              abc  : 1 match
              abcd : 2 matches


"""

result = re.findall("...", text)
result = re.findall("Py..on", text)

"""
    ^ - Checks whether the string starts with the given characters.

    ^a => a:    1 match
          abc:  1 match
          bac:  No match

"""

result = re.findall("^P",text)


"""
    $ - Checks whether the string ends with the given character.

    a$ => a      : 1 match
          lamba  : 1 match
          Python : No match

"""

result = re.findall("s$",text)
result = re.findall("hours$",text)
result = re.findall("hourss$",text)

"""
     * - Checks whether a character appears zero or more times.

         ma*n => mn     : 1 match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (n is not right after the a's)
"""
result = re.findall("sa*t",text)

"""
     + - Checks whether a character appears one or more times.

         ma+n => mn     : No match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (n is not right after the a's)
"""

result = re.findall("sa+t",text)

"""
    ? - Checks whether a character appears zero or one time.

        ma+n => mn     : No match
                man    : 1 match
                maaan  : 1 match
                main   : No match (n is not right after the a's)
"""

result = re.findall("sa?t",text)

"""
    {} - Checks how many times a character repeats.

        al{2}   => the letter l must repeat exactly 2 times after a.
        al{2,3} => the letter l must repeat 2 to 3 times after a.
        [0-9]{2,4} => a number with 2 to 4 digits.
"""
result = re.findall("a{2}", text)
result = re.findall("[0-9]{2}", text)

"""
    | - matches one of several alternatives.

        a|b => a or b

            cde =>    no match
            ade =>    1 match
            acdbea => 3 match
"""

"""
    () - used for grouping.

         (a|b|c)xz => xz must be preceded by one of a, b, or c.
"""



"""
    \ - lets us search for special characters literally.
        \$a => looks for the character a right after a literal $. In other
               words, $ is not interpreted by the regex engine as an anchor.

    \A - Checks whether the given characters are at the start of the string.
         \Athe => is "the" at the start of the string?

        result = re.findall("\APython", text)
        result = re.findall("hours\Z", text)

    \Z - Checks whether the given characters are at the end of the string.
         the\Z => does the string end with "the"?

    \b - Checks whether the given characters are at a word boundary.
         \bthe => is "the" at the start of a word?
         the\b => is "the" at the end of a word?

    \B - Checks whether the given characters are NOT at a word boundary.
         \Bthe => is "the" NOT at the start of a word?
         the\B => is "the" NOT at the end of a word?

    \d - same as [0-9], i.e. matches digits.
         \d => 12abc34

    \D - same as [^0-9], i.e. matches anything that is not a digit.
         \D => 1ab44_50

    \s - matches whitespace characters.
    \S - matches anything that is not whitespace.
    \w - matches letters, digits, and the underscore character.
    \W - the exact opposite of \w

"""


print(result)
