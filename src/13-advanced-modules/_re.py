# The re module is Python's tool for working with regular expressions
# ("regex") - a mini-language for describing PATTERNS of text (rather than
# exact text) so you can search for, extract, split on, or replace things
# like "any digit", "one or more letters", "a word at the start of a line",
# etc.
import re

# result = dir(re)

# re module

# Regex looked like magic symbols to me at first - these notes are how I made sense of it.
text = "Python Course: Your Python Programming Guide | 40 hours"

# re.findall()
# re.findall(pattern, string) scans the whole string and returns a list of
# EVERY piece of text that matches the pattern (not just the first one).

# result = re.findall("Python",text)
# The plain word "Python" as a pattern just matches that literal text - no
# special regex symbols involved yet. It appears twice in the sentence
# above ("Python Course" and "Your Python"), so this returns
# ["Python", "Python"].
# result = len(result)
# -> 2, the number of matches found.

# re.split()
# re.split(pattern, string) cuts the string into pieces everywhere the
# pattern matches, and returns the pieces as a list (the matched text itself
# is thrown away).

# result = re.split(" ", text)
# Splitting on a literal space breaks the sentence into its individual words:
# ["Python", "Course:", "Your", "Python", "Programming", "Guide", "|", "40", "hours"]
# result = re.split("R", text)
# Splitting on the capital letter "R" - regex is case-sensitive by default,
# and "R" only appears once, inside "Programming" -> ["Python Course: Your Python P", "ogramming Guide | 40 hours"]

# re.sub()
# re.sub(pattern, replacement, string) returns a NEW string with every match
# of the pattern swapped out for the replacement text (the original string
# itself is left unchanged, since strings are immutable in Python).

# result = re.sub(" ","-",text)
# Replaces every literal space with a hyphen:
# "Python-Course:-Your-Python-Programming-Guide-|-40-hours"
# result = re.sub("\s","-",text)
# "\s" (backslash-s) is a shorthand meaning "any whitespace character"
# (space, tab, newline, ...) - here it matches the same spaces as above, so
# the result looks the same for this particular sentence, but \s would also
# catch tabs/newlines if there were any.

# re.search()
# re.search(pattern, string) looks for the FIRST place the pattern matches
# anywhere in the string, and returns a "Match object" describing exactly
# where and what matched (or None if there's no match at all).

# result = re.search("Python",text)

# result = result.span()   # -> (0, 6): the (start, end) character indices of the match
# result = result.start()  # -> 0: the index where the match begins
# result = result.end()    # -> 6: the index right after the match ends
# result = result.group()  # -> "Python": the actual matched text
# result = result.string   # -> the original string that was searched

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

# text = "Python Course: Your Python Programming Guide | 40 hours"
# Each call below scans the whole "text" string above and collects every
# single CHARACTER (not whole word) that matches the bracket pattern.
result = re.findall("[abc]",text)
# Looks for any single occurrence of 'a', 'b', or 'c' - matches the two
# lowercase 'a's in "Programming" and "Guide" plus... walk through it
# yourself against the sentence to see which letters qualify.
result = re.findall("[sat]",text)
result = re.findall("[a-e]", text)
result = re.findall("[a-z]", text)
# Every individual lowercase letter in the sentence, one list entry per
# matched character (not grouped into words).
result = re.findall("[0-5]", text)
# Digits 0 through 5 - matches "4" and "0" from "40 hours" (as separate
# single-character matches, since [0-5] only ever matches ONE character at
# a time).
result = re.findall("[^abc]", text)
result = re.findall("[^0-9]", text)
# Every character that is NOT a digit - i.e. essentially the whole string
# minus the "4" and "0" in "40".

"""
    . - Matches any single character.

        .. => a    : No match
              ab   : 1 match
              abc  : 1 match
              abcd : 2 matches


"""

result = re.findall("...", text)
# Three dots in a row match any 3 consecutive characters (letters, spaces,
# punctuation - anything), chopping the whole string into non-overlapping
# groups of 3.
result = re.findall("Py..on", text)
# "Py" followed by any 2 characters followed by "on" matches "Python"
# (the 2 wildcard characters stand in for "th") - and it matches it twice,
# since "Python" appears twice in the sentence.

"""
    ^ - Checks whether the string starts with the given characters.

    ^a => a:    1 match
          abc:  1 match
          bac:  No match

"""

result = re.findall("^P",text)
# "^" anchors the match to the very beginning of the string - this matches
# because "text" literally starts with the capital letter "P" (in "Python").


"""
    $ - Checks whether the string ends with the given character.

    a$ => a      : 1 match
          lamba  : 1 match
          Python : No match

"""

result = re.findall("s$",text)
# "$" anchors the match to the very end of the string - "text" ends in
# "...40 hours", and the last character is "s", so this matches.
result = re.findall("hours$",text)
# Matches because the string literally ends with the word "hours".
result = re.findall("hourss$",text)
# No match - the string does not end with "hourss" (double s), so this
# returns an empty list [].

"""
     * - Checks whether a character appears zero or more times.

         ma*n => mn     : 1 match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (n is not right after the a's)
"""
result = re.findall("sa*t",text)
# 's' followed by zero-or-more 'a's followed by 't'. There is no "sat"-like
# substring in "text" (which has no adjacent s/a/t combination), so this
# returns an empty list [].

"""
     + - Checks whether a character appears one or more times.

         ma+n => mn     : No match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (n is not right after the a's)
"""

result = re.findall("sa+t",text)
# Same idea as "*" but requires AT LEAST one 'a' (zero is not enough) -
# still no match in this particular sentence.

"""
    ? - Checks whether a character appears zero or one time.

        ma+n => mn     : No match
                man    : 1 match
                maaan  : 1 match
                main   : No match (n is not right after the a's)
"""

result = re.findall("sa?t",text)
# 's' followed by zero-or-one 'a' followed by 't' - still no matching
# substring in this sentence, so an empty list.

"""
    {} - Checks how many times a character repeats.

        al{2}   => the letter l must repeat exactly 2 times after a.
        al{2,3} => the letter l must repeat 2 to 3 times after a.
        [0-9]{2,4} => a number with 2 to 4 digits.
"""
result = re.findall("a{2}", text)
# Requires TWO consecutive 'a' characters - "text" has no doubled 'a', so
# this returns an empty list.
result = re.findall("[0-9]{2}", text)
# A run of exactly 2 consecutive digits - matches "40" from "40 hours" (the
# characters '4' and '0' sitting right next to each other).

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
