# 34 Birthday Json
# Author: Christian Million
# Started: 2020-08-18
# Completed: 2020-08-18
# Last Modified: 2020-08-18
#
# Prompt: https://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html
#
# This exercise is Part 2 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 3, and Part 4.
# 
# In the previous exercise we created a dictionary of famous scientists’ birthdays. In this exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program.
# 
# Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and update the JSON file you have on disk with the scientist’s name. If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.
import json

with open('practice-python/resources/tng_birthdays.json', 'r') as json_file:
    tng_birthdays = json.load(json_file)

print("Welcome to the Birthday Dictionary! We know the birthdays of:")
for cast in tng_birthdays.keys():
    print("\t-", cast)

char = input('Who\'s birthday do you want to look up?\n')

if(char in tng_birthdays.keys()):
    print(f'{char}\'s birthday is: {tng_birthdays[char]}')
else:
    print(f'Sorry, I couldn\'t find an entry for {char}. Check to see if your spelled it right?')

if input("Do you want to add a birthday?(y/n)\n").lower()[0] == 'y':
    name = input("Okay! What is their name?\n")
    bd = input("And what is their birthday?(mm/dd/yyyy):\n")

    tng_birthdays[name] = bd

    with open('practice-python/resources/tng_birthdays.json', 'w') as json_w_file:
        json.dump(tng_birthdays, json_w_file)

    print(f'Awesome! {name}\'s Birthday ({bd}) was added.')
