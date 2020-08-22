# 06 String Lists
# Author: Christian Million
# Started: 2020-08-21
# Completed: 2020-08-21
# Last Modified: 2020-08-22
#
# Prompt: https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
#
# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

# Request a string from the user
inputString = input("Gimme a string and I'll tell you whether it's a palindrome or not:\n")

# First we turn the string into lower case
# And compare it against the string reversed (in lower case)
# In 'slicing' string[start:end:step], so string[::-1] means step through the whole thing in reverse
if(inputString.lower() == inputString[::-1].lower()):
    print(f'{inputString} is a palindrome! Backwards, it spells {inputString[::-1]}.')
else:
    print(f'{inputString} is NOT a palindrome. Backwards, it spells {inputString[::-1]}.')