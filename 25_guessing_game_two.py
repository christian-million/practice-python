# 25 Guessing Game Two
# Author: Christian Million
# Started: 2020-08-23
# Completed: 2020-08-23
# Last Modified: 2020-08-24
#
# Prompt: https://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html
#
# In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.
# 
# This time, we’re going to do exactly the opposite.
# You, the user, will have in your head a number between 0 and 100.
# The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
# 
# At the end of this exchange, your program should print out how many guesses it took to get your number.
# 
# As the writer of this program, you will have to choose how your program will strategically guess.
# A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number.
# But that’s not an optimal guessing strategy.
# An alternate strategy might be to guess 50 (right in the middle of the range), and then increase / decrease by 1 as needed.
# After you’ve written the program, try to find the optimal strategy! (We’ll talk about what is the optimal one next week with the solution.)

# My intended strategy is to guess a number in the middle of the highest and lowest possible values.
# If my guess needs to be higher, then that guess should become the 'lowest' possible answer
# If my guess needs to be lower, then that guess should become the 'highest' possible answer.


# Inititalize
guessCount = 0
correct = False
minVal = 0
maxVal = 100

# Helper function to get middle of two numbers
def getMiddle(small, large):
    return (small+large)//2

# Prompt user to think of a number.
print(f"Okay, think of a number between {minVal} and {maxVal}:")
input("Hit `Enter` when you've thought of the number!\n")

# Inititalize first guess as middle of minVal and maxVal
next_guess = getMiddle(minVal, maxVal)

while not correct:
    # Increase Guess Count
    guessCount += 1

    # Make my guess to the user and ask whether it is correct, or if I need to go higher or lower?
    resp = input(f"My next guess is {next_guess}.\nIs that correct (c) or should I guess higher(h) or lower(l)?\n").lower()[0]
    
    # If I need to go higher, reset minVal and make new guess
    if(resp == 'h'):
        minVal = next_guess + 1
        next_guess = getMiddle(minVal, maxVal)

    # If I need to go lower, reset maxVal and make new guess
    elif(resp == 'l'):
        maxVal = next_guess - 1 
        next_guess = getMiddle(minVal, maxVal)

    # Otherwise, I'll just assume I won.
    else:
        print(f"Yay!!! That only took me {guessCount} guesses.")
        break

print('Goodbye!')    