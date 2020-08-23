# 13 Fibonacci
# Author: Christian Million
# Started: 2020-08-22
# Completed: 2020-08-22
# Last Modified: 2020-08-23
#
# Prompt: https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
#
# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence
# is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

# Create a function to get a valid integer
def getValidInt(strPrompt, strWarn):
    while True:
        try:
            return int(input(strPrompt))
        except:
            print(strWarn)

def fibonacci(n):
    # Create a list to store the results
    seq=[]
    for i in range(n):
        # The first two should be 1
        if(len(seq) < 2):
            seq.append(1)
        # Otherwise, add the previous two nums
        else:
            seq.append(seq[i - 2] + seq[i - 1])
    return seq

# Request input from user
userNum = getValidInt("How many numbers in the Fibonnaci sequence do you want?\n", "Whoops! Must be a whole number!")

# Print results
print(fibonacci(userNum))