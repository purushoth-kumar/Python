# Generate a random number between 1 and 9 (including 1 and 9).
#Ask the user to guess the number, then tell them whether they guessed too low,
#too high, or exactly right.
import random
guess = random.randint(1, 9)
test = int(input("Guess a number between 1 and 9: "))
if guess == test:
    print('You have guessed the correctly!!')
else:
    guess = str(guess)
    print('You guessed wrong! The computer chose : ' + guess)
