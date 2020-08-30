# 35 Birthday Months
# Author: Christian Million
# Started: 2020-08-18
# Completed: 2020-08-18
# Last Modified: 2020-08-18
#
# Prompt: https://www.practicepython.org/exercise/2017/02/28/35-birthday-months.html
#
# This exercise is Part 3 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 2, and Part 4.
# 
# In the previous exercise we saved information about famous scientists’ names and birthdays to disk. In this exercise, load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday in each month.
# 
# Your program should output something like:
# 
# {
# 	"May": 3,
# 	"November": 2,
# 	"December": 1
# }

# Import libraries
import json
from collections import Counter
import datetime

# 'with' opens a resource manager (google says better that using open() and close())
with open('practice-python/resources/tng_birthdays.json', 'r') as json_file:
    tng_birthdays = json.load(json_file)

# Converts the "m/d/y" strings to python dates, then extracts month (%b)
months = [datetime.datetime.strptime(i, '%m/%d/%Y').strftime('%b') for i in tng_birthdays.values()]

# Counter counts each value in a list
c = Counter(months)

print(c)