'''
   Try to make the user guess a number randomly generated between
   1 and 100, using "higher"/"lower" hints. (attempts = 5)
   ** Search "python random" to learn about the "random module".
   ** Score out of 100. Each question is worth 20 points.
   ** Ask the user how many attempts they get and score each question
      based on the given number of lives.
'''

# random is another standard-library module (ships with Python) that
# provides tools for generating random values.
import random

# random.randint(a, b) returns a random whole number between a and b,
# with BOTH ends included -- unlike range(a, b), where b is excluded.
# So randint(1, 10) can actually return 10, whereas range(1, 10) would
# stop at 9. Note this line uses 1-10, even though the exercise
# description above asks for 1-100 -- worth keeping in mind if you're
# trying to match the written spec exactly.
number = random.randint(1, 10)
lives = int(input('how many attempts do you want: '))
attempts_left = lives
counter = 0

# Loop until either the user runs out of attempts (attempts_left reaches
# 0) or they guess correctly and `break` exits early.
while attempts_left > 0:
    attempts_left -= 1
    counter += 1
    guess = int(input('guess: '))

    if number == guess:
        # Scoring formula: start at 100, and subtract (100/lives) points
        # for every wrong guess made before this correct one.
        # (counter-1) is exactly the number of PREVIOUS (wrong) guesses,
        # since counter was just incremented for this, the successful,
        # guess. Guessing correctly on the very first try (counter == 1)
        # means (counter-1) == 0, so no points are subtracted and the
        # score is a perfect 100.
        print(f'Congrats, you got it on try {counter}. Your total score: {100 - (100/lives) * (counter-1)}')
        # break exits the while loop immediately, skipping any remaining
        # iterations -- there's no need to keep asking once the number
        # has been found.
        break
    elif number > guess:
        print('higher')
    else:
        print('lower')

    # This only ever fires on the very last allowed attempt, immediately
    # after attempts_left was decremented to 0 above -- so it announces
    # "out of attempts" exactly once, right as the loop is about to end
    # on its own (the while condition `attempts_left > 0` will now be
    # False on the next check).
    if attempts_left == 0:
        print(f'out of attempts. The number was: {number}')
