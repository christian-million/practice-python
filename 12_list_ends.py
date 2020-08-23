# 12 List Ends
# Author: Christian Million
# Started: 2020-08-22
# Completed: 2020-08-22
# Last Modified: 2020-08-23
#
# Prompt: https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
#
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

# Initialize a toy list
a = [5, 10, 15, 20, 25]

# Define a function that returns the first and last elements.
def firstLast(x):
   return [x[0], x[-1]]

# Print the results
print(firstLast(a))