# error handling

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as e:
#     print('you entered wrong info')
#     print(e)

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except:
#     print('you entered wrong info')

# Learned that else runs only when no exception was raised, and finally
# always runs, even after break.
while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as ex:
        print('you entered wrong info', ex)
    else:
        break
    finally:
        print('try except finished.')
