# x = 10

# if x > 5:
#     raise Exception("x cannot be greater than 5.")

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

# password = "1234567aA_"

# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("valid password: else")
# finally:
#     print("validation finished.")


# Learned that raising a plain Exception from __init__ stops the object
# from ever being created.
class Person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception("name field has too many characters.")
        else:
            self.name = name

p = Person("Aliiiiiiiiiiii", 1989)
