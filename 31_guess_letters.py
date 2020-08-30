# 31 Guess Letters
# Author: Christian Million
# Started: 2020-08-18
# Completed: 2020-08-18
# Last Modified: 2020-08-18
#
# Prompt: https://www.practicepython.org/exercise/2017/01/02/31-guess-letters.html
#
# This exercise is Part 2 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 3.
# 
# Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the player has to guess, letter by letter. The player guesses one letter at a time until the entire word has been guessed.
# (In the actual game, the player can only guess 6 letters incorrectly before losing).
# 
# Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly.
# For now, let the player guess an infinite number of times until they get the entire word.
# 
# As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess that letter again.
# Remember to stop the game when all the letters have been guessed correctly! Don’t worry about choosing a word randomly or keeping track of the number of guesses the player has remaining - we will deal with those in a future exercise.
# 
# An example interaction can look like this:
# 
# >>> Welcome to Hangman!
# _ _ _ _ _ _ _ _ _
# >>> Guess your letter: S
# Incorrect!
# >>> Guess your letter: E
# E _ _ _ _ _ _ _ E
# ...
# And so on, until the player gets the word.

def show(word, guesses):
    out = ''
    for letter in word:
        if letter in guesses:
            out += letter + " "
        else:
            out += "_ "
    return out

# Initialize
my_word = 'CATBIRD'
my_guesses = []
error_count = 0
slots = show(my_word, my_guesses)

while error_count < 6:

    print(slots)

    valid_guess = False

    while not valid_guess:
        next_guess = input("Guess Letter:\n").upper()
        
        if next_guess in my_guesses:
            print(f"Whoops! You've already guessed {next_guess}. Try again!")
            print(f"*psst.* As a reminder, here are your guesses so far: {my_guesses}")
        else:
            valid_guess = True

    my_guesses.append(next_guess)
    
    slots = show(my_word, my_guesses)

    if next_guess in my_word:
        print("Nice! Good job!")
        if(my_word == slots.replace(' ', '')):
            print(f"Congrats! You won with {error_count} errors.")
            break
    else:
        print("Ouch! That's not a correct letter.")
        error_count += 1

    
if(error_count == 6):
    print(f"Sorry! You ran out of guesses. The word was {my_word}.")