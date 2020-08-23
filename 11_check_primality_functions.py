# 11 Check Primality Functions
# Author: Christian Million
# Started: 2020-08-22
# Completed: 2020-08-22
# Last Modified: 2020-08-22
#
# Prompt: https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
#
# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you. Take this
# opportunity to practice using functions, described below.

# Create a function to get a valid integer
def getValidInt(strPrompt, strWarn):
    while True:
        try:
            return int(input(strPrompt))
        except:
            print(strWarn)

# Create a funtion to get a list of divisors of a number
def isPrime(num):
    # 1, 0, and negative number are not prime
    if(num <= 1):
       return False
    # If any number between 2 and the number is evenly divisible, it is not prime
    elif(any([True for i in range(2, num) if num%i==0])):
        return False
    # Else Prim!
    else:
        return True
        
# Request a valid integer from the user.
userInt = getValidInt("Enter a whole number:\n", "Whoops! Make sure it is a whole number!")

# Compare actual divisors with 'prime' divisors
if(isPrime(userInt)):
    print(f'Congratulations! {userInt} is prime!')
else:
    print(f'Ew. {userInt} is not prime.')