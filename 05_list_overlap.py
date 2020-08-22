# 05 List Overlap
# Author: Christian Million
# Started: 2020-08-21
# Completed: 2020-08-21
# Last Modified: 2020-08-22
#
# Prompt: https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
#
# Take two lists, say for example these two:
# 
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# and write a program that returns a list that contains only the elements that are common
# between the lists (without duplicates). Make sure your program works on two lists of different sizes.
# 
# Extras:
# 
# 1. Randomly generate two lists to test this
# 2. Write this in one line of Python
#   (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

# Import `randint` from the random library
from random import randint

# Randomly generate two lists to compare
# Uses list comprehension
a = [randint(1, 10) for i in range(1, randint(2,10))]
b = [randint(1, 10) for i in range(1, randint(2,10))]

# Return the randomly generated lists
print(a)
print(b)

# Return a Set Comprehension
# A set can only have unique values.
c = {i for i in a if i in b}
