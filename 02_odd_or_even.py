# 02 Odd Or Even
# Author: Christian Million
# Started: 2020-08-21
# Completed: 2020-08-21
# Last Modified: 2020-08-22
#
# Prompt: https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
#
# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user. Hint: how does an even / odd
# number react differently when divided by 2?
# 
# Extras:
# 
# - If the number is a multiple of 4, print out a different message.
# - Ask the user for two numbers: one number to check (call it num) and
# one number to divide by (check). If check divides evenly into num,
# tell that to the user. If not, print a different appropriate message.

# Initialize
validNumber = False
validCheck = False

# Until they provide me with a valid number, keep asking:
while not(validNumber):
    # if input can't be converted to integer, throw exception
    try:
        inputNumber = int(input("Please give me a whole number:\n"))
        validNumber = True
    except:
        print("Whoah! It has to be a whole number.")

# Until they provide me with a valid number, keep asking:
while not(validCheck):
    # if input can't be converted to integer, throw exception
    try:
        inputCheck = int(input("Which number should we see check?:\n"))
        validCheck = True
    except:
        print("Whoah! It has to be a whole number.")

# Check to see if number divides nicely into one another
if(inputNumber % inputCheck == 0):
    print(f"{inputCheck} fits nicely into {inputNumber}!")

    # Check to see if it fits nicely into 4
    if(inputNumber % 4 == 0):
        print(f'And {inputNumber} is divisible by 4!')
    
    # Check if it is even
    if(inputNumber % 2 == 0):
        print(f'And {inputNumber} is even.')
else:
    print(f'Ew. {inputCheck} does not sit well with {inputNumber}.')
