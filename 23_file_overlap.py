# 23 File Overlap
# Author: Christian Million
# Started: 2020-08-23
# Completed: 2020-08-23
# Last Modified: 2020-08-24
#
# Prompt: https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html
#
# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.
#
# (If you forgot, prime numbers are numbers that can’t be divided by any other number.
# And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example, which I will describe below.)

# Initialize path to files
path_prime = 'practice-python/resources/primenumbers.txt'
path_happy = 'practice-python/resources/happynumbers.txt'

# Open file, read each line, strip the trailing '\n', and convert to a set of integers
with open(path_prime, 'r') as rawPrime:
    primeList = {int(lines.rstrip()) for lines in rawPrime.readlines()}

# Open file, read each line, strip the trailing '\n', and convert to a set of integers
with open(path_happy, 'r') as rawHappy:
    happyList = {int(lines.rstrip()) for lines in rawHappy.readlines()}

# Check the intersection of the the two set and cast to list
same = list(primeList.intersection(happyList))

# Sort the list
same.sort()

# Return results to user.
print(same)