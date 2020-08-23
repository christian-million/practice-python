# 20 Element Search
# Author: Christian Million
# Started: 2020-08-18
# Completed: 2020-08-18
# Last Modified: 2020-08-18
#
# Prompt: https://www.practicepython.org/exercise/2014/11/11/20-element-search.html
#
# Write a function that takes an ordered list of numbers
# (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
# 
# Extras:
# 
# Use binary search.

a = [1, 5, 10, 25, 30, 45, 88, 90, 101]

def contains(target, l):
    return target in l

print(contains(9, a))
