# name = 'Ozan Ulas Sivaci'

# for letter in name:
#     if letter == 'a':
#         continue
#     print(letter)

# x = 0

# while x < 5:
#     x+=1
#     if x == 2:
#         continue
#     print(x)


# 1- Sum of odd numbers up to 100

x = 0
result = 0

while x <= 100:
    x += 1
    if x % 2 == 0:
        continue
    result += x

print(f'total: {result}')
