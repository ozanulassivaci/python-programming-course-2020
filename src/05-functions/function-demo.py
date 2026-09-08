# 1- Write a function that prints a given word a given number of times.

# def print_word(word, count):
#     print(word * count)

# print_word('Hello\n', 10)
# String repetition ("*") combined with a function parameter: repeating
# 'Hello\n' 10 times prints "Hello" on 10 separate lines (thanks to the
# embedded newline in the string being repeated too).


# 2- Write a function that turns any number of arguments passed to it
#    into a list.

# def convert_to_list(*params):
#     result_list = []

#     for param in params:
#         result_list.append(param)

#     return result_list

# result = convert_to_list(10,20,30,'Hello')

# print(result)
# *params already collects the arguments into a tuple automatically; this
# function's job is just to turn that tuple into a list instead (in
# practice, list(params) would do the same thing in one step).


# 3- Find every prime number between two given numbers.

# def find_primes(number1, number2):
#     for number in range(number1, number2+1):
#         if number > 1:
#             for i in range(2, number):
#                 if (number % i == 0):
#                     break
#             else:
#                 print(number)
# The "for...else" here is a lesser-known Python feature: the `else`
# block after a for loop runs ONLY IF the loop completed normally,
# without hitting a `break`. So this prints `number` only when the inner
# loop searched every possible divisor and never found one that divides
# evenly (never broke) -- i.e. exactly when `number` is prime.

# number1 = int(input('number 1:'))
# number2 = int(input('number 2:'))

# find_primes(number1, number2)



# 4- Return the exact divisors of a given number as a list.


def find_divisors(number):
    divisors = []

    # Check every candidate from 2 up to (not including) number itself;
    # anything that divides evenly (remainder 0) is a divisor.
    for i in range(2, number):
        if (number % i == 0):
            divisors.append(i)

    # return sends the finished list back to whoever called the function
    # -- without it, the function would implicitly return None instead.
    return divisors


# 20's divisors between 2 and 19 are 2, 4, 5, and 10 (2*10=20, 4*5=20).
print(find_divisors(20))  # [2, 4, 5, 10]
