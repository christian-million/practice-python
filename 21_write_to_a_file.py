# 21 Write To A File
# Author: Christian Million
# Started: 2020-08-23
# Completed: 2020-08-23
# Last Modified: 2020-08-24
#
# Prompt: https://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html
#
# Take the code from the How To Decode A Website exercise
# (if you didn’t do it or just want to play with some different code, use the code from the solution),
# and instead of printing the results to a screen, write the results to a txt file.
# In your code, just make up a name for the file you are saving to.
# 
# Extras:
# 
# - Ask the user to specify the name of the output file that will be saved.

# Load requests library to get text from a webpage
import requests

# Initialize url to target webpage
base_url = 'https://www.christianmillion.com'

# Call a request to url to get all text from website
r = requests.get(base_url)

# prompt user for filename
filename = input("Name the file:\n")

# `with` here is a resource manager. Good for connections (files / database / etc.)
# It will close smartly
# Write returned request to a file in the path practice-python/out/{}.txt
with open('practice-python/out/' + filename + '.txt', 'w') as open_file:
    open_file.write(r.text)