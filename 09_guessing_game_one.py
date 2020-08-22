# 09 Guessing Game One
# Author: Christian Million
# Started: 2020-08-21
# Completed: 2020-08-21
# Last Modified: 2020-08-22
#
# Prompt: https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
#
# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)
# 
# Extras:
# 
# 1. Keep the game going until the user types “exit”
# 2. Keep track of how many guesses the user has taken, and when the game ends, print this out.

# Import
from random import randint

# Initialize
exit = False

# Go until they say 'exit'
while not(exit):

    # Initialize new guessing game
    guessCount = 0
    targetNum = randint(1, 100)
    correct = False

    # Until they guess the correct number keep prompting with clues!
    while not(correct):
        guess = input("Guess the number:\n")

        if(guess == 'exit'):
            exit = True
            break

        # Try to turn their guess into an integer.
        try:
            guess = int(guess)
        except:
            print('I\'m not sure what you guessed. So I\'ll guess for you.')
            print('Next time make sure you provide an integer or \'exit\'.')
            guess = randint(1, 100)

        # Add a guess to the guessCount!
        guessCount = guessCount + 1

        # Check whether too high, too low, or juuuust right.
        if(guess<targetNum):
            print("Too Low!")
        elif(guess>targetNum):
            print("Too High!")
        else:
            correct = True
            print(f"You guessed it! It took {guessCount} guesses.")
            print(f"Let's play again!\nOr type 'exit' at any time to exit.")

# Send your farewells to the user.
print("Goodbye!")


