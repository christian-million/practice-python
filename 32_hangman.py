# 32 Hangman
# Author: Christian Million
# Started: 2020-08-18
# Completed: 2020-08-18
# Last Modified: 2020-08-18
#
# Prompt: https://www.practicepython.org/exercise/2017/01/10/32-hangman.html
#
# This exercise is Part 3 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 2.
# 
# You can start your Python journey anywhere, but to finish this exercise you will have to have finished Parts 1 and 2 or use the solutions (Part 1 and Part 2).
# 
# In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.
# 
# In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for guessing the letter and displaying that information to the user. In this exercise, we have to put it all together and add logic for handling guesses.
# 
# Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:
# 
# Only let the user guess 6 times, and tell the user how many guesses they have left.
# Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
# Optional additions:
# 
# When the player wins or loses, let them start a new game.
# Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman. This is challenging - do the other parts of the exercise first!
# Your solution will be a lot cleaner if you make use of functions to help you!

# Import choice from random
from random import choice

# Function to get a random word from list of words
def get_word(path = 'practice-python/resources/sowpods.txt'):
    with open(path) as word_file:
        word = choice([line.rstrip() for line in word_file.readlines()])
    return word

# Draws the hangman board game with `num` number of errors
def noose(num = 0):

    opts = {0: [" ", " ", " ", " ", " ", " "],
            1: ["O", " ", " ", " ", " ", " "],
            2: ["O", "\\", " ", " ", " ", " "],
            3: ["O", "\\", "/", " ", " ", " "],
            4: ["O", "\\", "/", "|", " ", " "],
            5: ["O", "\\", "/", "|", "/", " "],
            6: ["O", "\\", "/", "|", "/", "\\"]}
    x = opts[num]
    print("   ________")
    print("   |      |")
    print(f"  {x[1]}{x[0]}{x[2]}     |")
    print(f"   {x[3]}      |")
    print(f"  {x[4]} {x[5]}     |")
    print("          |")
    print("    ------------")

# Displays available slots and correctly guessed letters
def show(word, guesses):
    out = ''
    for letter in word:
        if letter in guesses:
            out += letter + " "
        else:
            out += "_ "
    return out

# Initializes a new game
def new_game():
    my_word = get_word()
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
                print(f"The word was {my_word}. ")
                victory = 1
                break
        else:
            print("Ouch! That's not a correct letter.")
            error_count += 1
            noose(error_count)

    if(error_count == 6):
        print(f"Sorry! You ran out of guesses. The word was {my_word}.")
        victory = 0
    return victory


def main():
    print("WELCOME TO HANGMAN!")
    print("-------------------")
    input("Press Enter to Start!\n")

    keep_playing = True
    while keep_playing:
        print("Okay, I'm going to pick a random word...")
        last_outcome = new_game()
        flavor = "Nice Game!" if last_outcome == 1 else "Bummer :("
        if input(f"{flavor} Wanna play again?(y/n)\n").lower()[0] == 'n':
            keep_playing = False
    
    print("Bye! Thanks for the fun :)")




if __name__ == "__main__":
    main()