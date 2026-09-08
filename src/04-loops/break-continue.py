# name = 'Ozan Ulas Sivaci'

# "continue" immediately jumps back to the top of the loop for the NEXT
# iteration, skipping any code below it for the current one. Here, every
# time letter is 'a', the print() call is skipped -- so all letters get
# printed except every 'a'.
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
# Walking through this: x goes 1 (printed), 2 (continue skips the print),
# 3, 4, 5 (all printed) -- so this would print 1, 3, 4, 5, skipping only
# the 2.


# 1- Sum of odd numbers up to 100

x = 0
result = 0

# "while <condition>:" keeps re-running its indented block for as long as
# the condition stays True, re-checking it before every iteration.
while x <= 100:
    x += 1
    # continue here skips straight back to the `while x <= 100:` check
    # whenever x is even, so the `result += x` line below never runs for
    # even numbers -- only odd x values get added to result.
    if x % 2 == 0:
        continue
    result += x

# Careful trace of the loop boundary: the condition `x <= 100` is checked
# using the OLD value of x, before x += 1 runs -- so when x is 100 at the
# top of the loop, the condition is still True, and x gets incremented to
# 101 (which is odd) and added to result, before the NEXT check
# (101 <= 100) finally stops the loop. So this actually sums every odd
# number from 1 through 101, not just up to 100 -- a classic off-by-one
# result of incrementing before checking. The total printed is 2601, not
# 2500 (which would be the sum of odd numbers 1 through 99).
print(f'total: {result}')
