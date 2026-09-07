# up to 100

# x = 1
# while x <= 100:
#     if x % 2==1:
#         print(f'odd number: {x}')
#     else:
#         print(f'even number: {x}')
#     x += 1

# print('done...')


name = ''  # False
# Tried this with just `not name.strip()` first, but isspace() reads
# cleaner for "did the user just mash the space bar".
while name.isspace():
    name = input('enter your name: ')

print(f'Hello, {name}')
