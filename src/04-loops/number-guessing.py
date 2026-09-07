'''
   Try to make the user guess a number randomly generated between
   1 and 100, using "higher"/"lower" hints. (attempts = 5)
   ** Search "python random" to learn about the "random module".
   ** Score out of 100. Each question is worth 20 points.
   ** Ask the user how many attempts they get and score each question
      based on the given number of lives.
'''

import random

number = random.randint(1, 10)
lives = int(input('how many attempts do you want: '))
attempts_left = lives
counter = 0

while attempts_left > 0:
    attempts_left -= 1
    counter += 1
    guess = int(input('guess: '))

    if number == guess:
        print(f'Congrats, you got it on try {counter}. Your total score: {100 - (100/lives) * (counter-1)}')
        break
    elif number > guess:
        print('higher')
    else:
        print('lower')

    if attempts_left == 0:
        print(f'out of attempts. The number was: {number}')
