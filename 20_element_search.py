# 20 Element Search
# Author: Christian Million
# Started: 2020-08-23
# Completed: 2020-08-23
# Last Modified: 2020-08-24
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

# Initialize Practice Ordered List
a = [1, 5, 10, 25, 30, 45, 88, 90, 101]

# Checks if target is in original list (ol)
def contains(target, ol):
    return target in ol

# Extra binary search version
def binarySearch(x, ol):

    while True:
        # Find halfway point
        half_length = len(ol) // 2

        # If halfway point is equal to target then True!
        if(ol[half_length] == x):
            return True
        # If halfway point is last element and not target, then False!
        elif(len(ol) == 1 and ol[0] != x):
            return False
        # Else if halfway point is higher / lower, cut ol in half an start again
        else:
            if(ol[half_length] > x):
                ol = ol[:half_length]
            else:
                ol = ol[half_length:]

# Print results to terminal
print(contains(5,a))
print(binarySearch(5,a))