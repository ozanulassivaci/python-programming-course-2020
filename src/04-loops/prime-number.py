'''
Question: Find out whether an entered number is prime.
** A prime number is a number with no exact divisor other than
   1 and itself.
'''

number = int(input('number: '))
# Start by optimistically assuming the number IS prime, then look for any
# evidence that disproves it.
is_prime = True

# 1 is a special case: it's excluded from the definition of prime numbers
# by convention, even though it technically has no divisors between 1 and
# itself. The loop below wouldn't catch this on its own (range(2, 1) is
# empty), so it needs to be handled explicitly.
if number == 1:
    is_prime = False

# Try every candidate divisor from 2 up to (but not including) `number`
# itself. If ANY of them divides evenly (remainder 0), the number has a
# divisor other than 1 and itself, so it's not prime.
for i in range(2, number):
    if (number % i == 0):
        is_prime = False
        # No need to keep checking once we've already found one divisor
        # -- break exits the loop immediately.
        break

# Note an edge case this code doesn't explicitly handle: for number == 2,
# range(2, 2) is empty, so the loop never runs and is_prime correctly
# stays True (2 IS prime -- the smallest prime, and the only even one).
# But for number == 0 or a negative number, range(2, number) is ALSO
# empty (or invalid), so is_prime again stays True by default, even
# though 0 and negative numbers aren't prime -- this program would
# incorrectly call them "prime" since there's no explicit check ruling
# them out the way there is for 1.

if is_prime:
    print('the number is prime.')
else:
    print('the number is not prime.')
