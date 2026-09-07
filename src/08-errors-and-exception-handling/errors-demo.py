numbers = ["1", "2", "5a", "10b", "abc", "10", "50"]

# 1: Find the numeric values inside the list elements.

# for x in numbers:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue

# 2: Keep asking for input until the user enters 'q', making sure every
# input is a number, otherwise print an error message.

# while True:
#     number = input('number: ')
#     if number == 'q':
#         break

#     try:
#         result = float(number)
#         print('you entered: ', result)
#         break
#     except ValueError:
#         print('invalid number')
#         continue

# 3: Raise an error if the entered password contains Turkish characters.

# def check_password(password):
#     turkish_chars = 'şçğüöıİ'
#
#     for i in password:
#         if i in turkish_chars:
#             raise TypeError('Password cannot contain Turkish characters.')
#         else:
#             pass
#     print('valid password')

# password = input('password: ')

# try:
#     check_password(password)
# except TypeError as err:
#     print(err)

# 4: Build a factorial function and raise error messages for bad input.

# Learned that raising a ValueError lets the caller catch it with a
# regular try/except instead of the program crashing.
def factorial(x):
    x = int(x)

    if x < 0:
        raise ValueError('Negative value')

    result = 1

    for i in range(1, x + 1):
        result *= i

    return result

for x in [5, 10, 20, -3, '10a']:
    try:
        y = factorial(x)
    except ValueError as err:
        print(err)
        continue
    print(y)
