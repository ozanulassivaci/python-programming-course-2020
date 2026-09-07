# 1- Write a function that prints a given word a given number of times.

# def print_word(word, count):
#     print(word * count)

# print_word('Hello\n', 10)


# 2- Write a function that turns any number of arguments passed to it
#    into a list.

# def convert_to_list(*params):
#     result_list = []

#     for param in params:
#         result_list.append(param)

#     return result_list

# result = convert_to_list(10,20,30,'Hello')

# print(result)


# 3- Find every prime number between two given numbers.

# def find_primes(number1, number2):
#     for number in range(number1, number2+1):
#         if number > 1:
#             for i in range(2, number):
#                 if (number % i == 0):
#                     break
#             else:
#                 print(number)

# number1 = int(input('number 1:'))
# number2 = int(input('number 2:'))

# find_primes(number1, number2)



# 4- Return the exact divisors of a given number as a list.


def find_divisors(number):
    divisors = []

    for i in range(2, number):
        if (number % i == 0):
            divisors.append(i)

    return divisors


print(find_divisors(20))
