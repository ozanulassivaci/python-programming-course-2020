# x = 10

# if x > 5:
#     raise Exception("x cannot be greater than 5.")
# "raise Exception('message')" manually creates and throws a generic
# Exception with a custom message. Since x is 10 here (greater than 5),
# running this code would immediately stop the program (there's no
# try/except around it) and print a traceback ending in:
# "Exception: x cannot be greater than 5."

# def check_password(psw):
#     import re
#     if len(psw) < 8:
#         raise Exception("password must be at least 7 characters.")
#     elif not re.search("[a-z]", psw):
#         raise Exception("password must contain a lowercase letter.")
#     elif not re.search("[A-Z]", psw):
#         raise Exception("password must contain an uppercase letter.")
#     elif not re.search("[0-9]", psw):
#         raise Exception("password must contain a digit.")
#     elif not re.search("[_@$]", psw):
#         raise Exception("password must contain an alphanumeric character.")
#     elif re.search("\s",psw):
#         raise Exception("password must not contain whitespace.")
#     else:
#         print("valid password")
# "import re" brings in Python's built-in regular-expressions module,
# used here for pattern matching inside strings. re.search(pattern, psw)
# scans psw for any character matching `pattern`, returning a match
# object (which is "truthy") if found, or None (which is "falsy") if
# not. So "[a-z]" checks for any lowercase letter, "[A-Z]" for any
# uppercase letter, "[0-9]" for any digit, "[_@$]" for one of those three
# special characters, and "\s" for any whitespace character (space, tab,
# etc). check_password() checks these rules one at a time with
# elif -- as soon as one rule is violated, that specific raise fires and
# the function stops there (later elif branches are never reached for
# that call).

# password = "1234567aA_"

# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("valid password: else")
# finally:
#     print("validation finished.")
# Tracing through with password = "1234567aA_": length is 10 (>= 8, ok),
# contains a lowercase letter ('a', ok), an uppercase letter ('A', ok),
# a digit ('1', ok), one of '_@$' ('_', ok), and no whitespace -- so
# every elif check passes and check_password() falls through to its own
# "print('valid password')" inside the function. Since no exception was
# raised, the except block here is skipped, the else block runs
# ('valid password: else'), and finally always runs afterwards
# regardless ('validation finished.').


# Learned that raising a plain Exception from __init__ stops the object
# from ever being created.
class Person:
    def __init__(self, name, year):
        # If the check fails, raise stops __init__ partway through --
        # self.name is never set, and the Person object is never fully
        # constructed at all. The constructor doesn't need an explicit
        # "return" to stop; raise transfers control immediately to
        # whatever called Person(...), looking for a matching except.
        if len(name) > 10:
            raise Exception("name field has too many characters.")
        else:
            self.name = name

# "Aliiiiiiiiiiii" is 14 characters long, which is more than 10, so
# __init__ raises the Exception above. Because this call is NOT wrapped
# in a try/except anywhere in this file, the exception is never caught:
# it propagates all the way up and crashes the program, printing a
# traceback that ends with
# "Exception: name field has too many characters." -- `p` never actually
# gets created.
p = Person("Aliiiiiiiiiiii", 1989)
