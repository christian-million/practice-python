# 15 Reverse Word Order
# Author: Christian Million
# Started: 2020-08-22
# Completed: 2020-08-22
# Last Modified: 2020-08-23
#
# Prompt: https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
#
# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.
# For example, say I type the string:
#   
# 'My name is Michele'
#
# Then I would see the string:
#
# 'Michele is name My'
#
# shown back to me.

def str_rev(str):
   # splits a string into a list by the spaces
   # [::-1] Steps through the list from the end (reversing the string)
   r = str.split(' ')[::-1]

   # this joins each of the elements of the list by a " "
   return " ".join(r)

# Request a sentence from the user
x = input('sentence pleaaase:\n')

# Print results!
print(str_rev(x))