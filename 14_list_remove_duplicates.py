# 14 List Remove Duplicates
# Author: Christian Million
# Started: 2020-08-22
# Completed: 2020-08-22
# Last Modified: 2020-08-23
#
# Prompt: https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
#
# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
# 
# Extras:
# 
# - Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# - Go back and do Exercise 5 using sets, and write the solution for that in a different function.

# Unique Loop uses a loop to append unique values from a list
def uniqueLoop(x):
    out = []
    for i in x:
        if i not in out:
            out.append(i)
    return out

# Unique set uses the inherit properties of 'sets' to remove the duplicates from a list
# Is this cheating?
def uniqueSet(x):
    return list(set(x))

# Initialize a toy list
a = [1, 1, 2, 2, 3, 3, 3]


# Print results using both functions!
print(uniqueLoop(a))
print(uniqueSet(a))