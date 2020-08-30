# 30 Pick Word
# Author: Christian Million
# Started: 2020-08-18
# Completed: 2020-08-18
# Last Modified: 2020-08-18
#
# Prompt: https://www.practicepython.org/exercise/2016/09/24/30-pick-word.html
#
# This exercise is Part 1 of 3 of the Hangman exercise series. The other exercises are: Part 2 and Part 3.
# 
# In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary (http://norvig.com/ngrams/sowpods.txt).
# Download this file and save it in the same directory as your Python code. This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments. Each line in the file contains a single word.
# 
# Hint: use the Python random library for picking a random word.

from random import choice

# Initialize the path to words
path = 'practice-python/resources/sowpods.txt'

# Create a function to get a random word
def get_word(path = 'practice-python/resources/sowpods.txt'):
    # Opens the files
    with open(path) as word_file:
        # Randomly selects a word from the formatted word list
        word = choice([line.rstrip() for line in word_file.readlines()])
    return word

# Show user
print(get_word())