'''
Question: Find out whether an entered number is prime.
** A prime number is a number with no exact divisor other than
   1 and itself.
'''

number = int(input('number: '))
is_prime = True

if number == 1:
    is_prime = False

for i in range(2, number):
    if (number % i == 0):
        is_prime = False
        break

if is_prime:
    print('the number is prime.')
else:
    print('the number is not prime.')
