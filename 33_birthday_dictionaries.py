# 33 Birthday Dictionaries
# Author: Christian Million
# Started: 2020-08-18
# Completed: 2020-08-18
# Last Modified: 2020-08-18
#
# Prompt: https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html
#
# This exercise is Part 1 of 4 of the birthday data exercise series. The other exercises are: Part 2, Part 3, and Part 4.
# 
# For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based on their name. Create a dictionary (in your file) of names and birthdays. When you run your program it should ask the user to enter a name,
# and return the birthday of that person back to them. The interaction should look something like this:
# 
# >>> Welcome to the birthday dictionary. We know the birthdays of:
# Albert Einstein
# Benjamin Franklin
# Ada Lovelace
# >>> Who's birthday do you want to look up?
# Benjamin Franklin
# >>> Benjamin Franklin's birthday is 01/17/1706.
# Happy coding!

import json

birthday_dict = {"Patrick Stewart": "07/13/1940",
"Levar Burton": "02/16/1957",
"Jonathan Frakes": "08/19/1952",
"Gates McFadden": "03/02/1949",
"Michael Dorn": "12/09/1952",
"Brent Spiner": "02/02/1949",
}

with open('practice-python/resources/tng_birthdays.json', 'w') as json_file:
    json.dump(birthday_dict, json_file)

print("Welcome to the Birthday Dictionary! We know the birthdays of:")
for cast in birthday_dict.keys():
    print("\t-", cast)

char = input('Who\'s birthday do you want to look up?\n')

if(char in birthday_dict.keys()):
    print(f'{char}\'s birthday is: {birthday_dict[char]}')
else:
    print(f'Sorry, I couldn\'t find an entry for {char}. Check to see if your spelled it right?')
