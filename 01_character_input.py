# 01 Character Input
# Author: Christian Million
# Started: 2020-08-21
# Completed: 2020-08-21
# Last Modified: 2020-08-22
#
# Prompt: https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
#
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells
# them the year that they will turn 100 years old.
# 
# Extras:
# 
# 1. Add on to the previous program by asking the user for another number and
# printing out that many copies of the previous message.
# (Hint: order of operations exists in Python)
# 
# 2. Print out that many copies of the previous message on separate lines.
# (Hint: the string "\n is the same as pressing the ENTER button)

# Initialize Variables

# Age must be positive integer
validAge = False
validTime = False

# Hard code current year because prompt doesn't say we can use datetime package
currentYear = 2020 

# Request the users name
inputName = input("Tell me your name:\n")

# Until they give me a positive intiger - keep asking...
while not(validAge):
    try:
        inputAge = int(input(f"Thanks, {inputName}. Tell me your age:\n"))
        if(inputAge > 0):
            validAge = True
    except:
        print("Whoops! You're age should be a positive whole number!")

# Calculate the year they will turn 100
year100 = currentYear + (100 - inputAge)

# Create the message to send
msg = f'Woah, {inputName}, you will be 100 in the year {year100}!'

# Print the message!
print(msg)

# For extra credit ask them how many times to print the message
while not(validTime):
    try:
        inputTimes = int(input(f"Okay, {inputName}. Give me another number:\n"))
        if(inputTimes > 0):
            validTime = True
    except:
        print("Whoops! The number should be a positive whole number!")

print((msg+'\n')*inputTimes)