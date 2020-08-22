# 04 Divisors
# Author: Christian Million
# Started: 2020-08-21
# Completed: 2020-08-21
# Last Modified: 2020-08-22
#
# Prompt: https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
#
# Create a program that asks the user for a number and then prints out a list
# of all the divisors of that number. (If you don’t know what a divisor is,
# it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

# Initialize
validNum = False

# Get a valid integer
while not(validNum):
    try:
        targetNum = int(input("Please input a whole number:\n"))
        validNum = True
    except:
        print('a WHOLE NUMBER, please.')

# Use a list comprehension to get each number that divides nicely into the target number
# Reading left to right within the brackets, it says:
#   return divisor for each num in the range IF it there is no remainder.
divisors = [i for i in range(1, targetNum+1) if targetNum % i == 0]


print(divisors)