# 28 Max Of Three
# Author: Christian Million
# Started: 2020-08-18
# Completed: 2020-08-18
# Last Modified: 2020-08-18
#
# Prompt: https://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html
#
# Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!
# 
# The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!

# Sorts a lists and takes the last value
def max_of_three(a=1, b=2, c=3):
    x = [a, b, c]
    x.sort()
    return x[-1]

# Series of elif statements - Not easily scalable
def max_of_three_alt(a=1, b=2, c=3):
    
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    if c >= a and c >= b:
        return c

# Compares all each value against all of the other ones.
# If it is the largest, then it will be returned.
def max_of_three_alt1(a=1, b=2, c=3):
    x = [a, b, c]
    for i in x:
        if all([i >= j for j in x]):
            return i



print(max_of_three())
print(max_of_three_alt())
print(max_of_three_alt1())


print(max_of_three(a = 99, b = -4, c = 36))
print(max_of_three_alt(a = 99, b = -4, c = 36))
print(max_of_three_alt1(a = 99, b = -4, c = 36))