# 03 List Less Than Ten
# Author: Christian Million
# Started: 2020-08-21
# Completed: 2020-08-21
# Last Modified: 2020-08-22
#
# Prompt: https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
#
# Take a list, say for example this one:
# 
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 
# and write a program that prints out all the elements of the list that are less than 5.
# 
# Extras:
# 
# 1. Instead of printing the elements one by one, make a new list that has all the elements
#   less than 5 from this list in it and print out this new list.
# 2. Write this in one line of Python.
# 3. Ask the user for a number and return a list that contains only elements from the
#   original list a that are smaller than that number given by the user.

# Initialize
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
validNum = False

# Make sure the number is valid
while not(validNum):
    try:
        inputNum = int(input("Gimme Num:\n"))
        validNum = True
    except:
        print('C\'mon, gimme whole num!')


# To Do it in one line you need to use a 'list comprehension'
# List comprehension is:
# - An expression followed by
# - A for clause then
# - 0 or more for OR if clauses
lessNum = [a[i] for i in a if i < inputNum]

# Print the resulting list to user
print(lessNum)