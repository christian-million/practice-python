# 07 List Comprehensions
# Author: Christian Million
# Started: 2020-08-21
# Completed: 2020-08-21
# Last Modified: 2020-08-22
#
# Prompt: https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
#
# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and
# makes a new list that has only the even elements of this list in it.

# Initialize dummy list
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Find all elements that go evenly into two
# Using a list comprehension
b = [i for i in a if i % 2 == 0]

# Return result to user
print(b)