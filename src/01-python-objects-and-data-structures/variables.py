# A variable is just a name that points at a value stored in memory.
# You create one simply by assigning a value to a name with "=" -- there is
# no need to declare a type up front like in some other languages; Python
# figures out the type from the value itself (this is called "dynamic
# typing").
salary_ali = 5000
salary_ahmet = 4000
tax = 0.27          # 0.27 means 27%, i.e. 27 out of 100

# Operator precedence rules apply just like in normal math: the parentheses
# force (salary_ali * tax) to be computed first (that's "how much tax to
# pay"), and only then is the result subtracted from the salary.
# For salary_ali: 5000 - (5000 * 0.27) = 5000 - 1350 = 3650 (take-home pay).
print(salary_ali - (salary_ali * tax))
# For salary_ahmet: 4000 - (4000 * 0.27) = 4000 - 1080 = 2920.
print(salary_ahmet - (salary_ahmet * tax))

# Variable naming rules
# - Names can contain letters, digits and underscores, but...

# can't start with a digit
# e.g. "1number" would be a SyntaxError -- Python needs the first character
# to be a letter or an underscore so it can tell a name apart from a number
# literal.

number1 = 10
print(number1)

# Variables aren't fixed once created -- reassigning simply makes the name
# point at a new value. The old value (10) is discarded (garbage collected)
# since nothing refers to it anymore.
number1 = 20
print(number1)

# += is a shorthand ("augmented assignment") for "take the current value,
# add something to it, and store the result back in the same name".
# number1 += 30  is exactly the same as  number1 = number1 + 30
# number1 is 20 here, so after this line it becomes 20 + 30 = 50.
number1 += 30
print(number1)

# Case sensitivity
# Python treats uppercase and lowercase letters as completely different
# characters, so "age" and "AGE" are two separate, independent variables --
# not the same variable written two different ways.

age = 20
AGE = 30

print(age)  # 20
print(AGE)  # 30

# Better to stick with plain ASCII letters in identifiers
# Python does technically allow unicode letters in names (like "yaş"), but
# sticking to plain a-z/A-Z/0-9/_ avoids encoding headaches and keeps code
# portable and easy for every editor/terminal to display correctly.

year = 20
# A leading underscore is a common convention meaning "this is somewhat
# internal / not meant to be used from outside" -- it's just a naming
# convention, Python doesn't enforce anything special because of it here.
_age = 20

# Every value in Python has a type, even though you never wrote the type
# down yourself -- Python infers it from the literal on the right-hand side.
x = 1                 # int    -> a whole number
y = 2.3                # float  -> a number with a decimal point
name = "Kerem"         # string -> text, wrapped in quotes
is_student = True      # bool   -> True or False (note the capital letters)

# Python also supports "tuple unpacking": assigning several variables at
# once from a comma-separated group of values, matched up in order.
# x, y, name, is_student = (1, 2.3, "Kerem", True)

# Careful: quoting a number makes it a *string*, not an int -- '10' is text
# that happens to look like a number, it is not the number 10.
a = '10'
b = '20'
# Because a and b are strings, "+" here does NOT do arithmetic addition;
# for strings "+" means concatenation (glue the two pieces of text
# together). So '10' + '20' produces the 4-character string '1020', not
# the number 30.
print(a+b)  # => 1020

first_name = "Ozan"
last_name = " Sivaci"  # note the leading space, so the join reads naturally

# Again, "+" concatenates strings end-to-end. Since last_name already starts
# with a space, we don't need to add one here ourselves.
print(first_name + last_name)  # Ozan Sivaci
