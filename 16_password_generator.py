# 16 Password Generator
# Author: Christian Million
# Started: 2020-08-22
# Completed: 2020-08-22
# Last Modified: 2020-08-23
#
# Prompt: https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
#
# Write a password generator in Python.
# Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password. 
# Include your run-time code in a main method.
# 
# Extra:
# 
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

# Import the Random Library!
import random

# Create a dictionary of different types of symbols for use in the password
opts = {'alpha': 'abcdefghijklmnopqrstuvwxyz',
        'alphaCap': 'abcdefghijklmnopqrstuvwxyz'.upper(),
        'num': '0123456789',
        'sym': '!-_@#$%&'}

# Create a function to randomly divide a number into random groups
# This is to create random `weights` for each of the elements in `opts`
def group_divide(num, parts):
    # Can't divide num into parts > num
    if(parts > num):
         return None
    # Ends recursive and its easy to dived nums into 1 part
    if(parts == 1):
        return [num]
    # Else return a random num between 1 and num-parts (this is so each 'part' has at least 1 in it)
    else:
        x = random.randint(1, num - parts)
        groups = [x] + group_divide(num - x, parts - 1)

    return(groups)

# Create a function that generates a password to a specified length
def gen_password(length):
    # Create weights for alpha, alphaCap, num, and symbols
    weights = group_divide(length, 4)

    # Make it random because I THINK `group_divide` is larger the lower the index
    random.shuffle(weights)

    # Select `weight` characters with replacement from each opts.values
    # I wonder if this can be done with ZIP
    # ALTERNATIVE APPROACH : chars = map(lambda x,y: random.choices(population = x, k = y), opts.values(), weights)
    chars = []
    for eachOpt, eachWeight in zip(opts.values(), weights):
        chars.append(random.choices(eachOpt, k = eachWeight))

    # The above returns a list of lists - this flattens it to just a list
    flatChar = [item for i in chars for item in i]

    # Randomize elements in the list
    random.shuffle(flatChar)

    # Turn into a single string
    password = "".join(flatChar)
    
    # Return the password
    return(password)

def main():
    # Initialize
    strength = input('Would you like a strong(s) or weak(w) password:\n')[0].lower()
    MINCHAR = 6
    MAXCHAR = 15

    if(strength == 'w'):
        # Choose a weak ass password
        pswd = random.choice(['123456', 'password', '000000', 'abc123'])

    else:
        # Generate random length
        pswdLen = random.randint(MINCHAR, MAXCHAR)
        # Generate the password
        pswd = gen_password(pswdLen)

    print(pswd)

# If a script is run (rather than imported), run the main method.
if __name__ == '__main__':
    main()
