# 22 Read From File
# Author: Christian Million
# Started: 2020-08-23
# Completed: 2020-08-23
# Last Modified: 2020-08-24
#
# Prompt: https://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html
#
# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. I have a .txt file for you, if you want to use it!
# 
# Extra:
# 
# Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and count how many of each “category” of each image there are.
# This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images.
# Once you take a look at the first line or two of the file, it will be clear which part represents the scene category.
# To do this, you’re going to have to remember a bit about string parsing in Python 3. I talked a little bit about it in this post.

# Initialize path to file
path = 'practice-python/resources/nameslist.txt'

# Open file, read in all lines, and strip the '\n' at the end.
with open(path, 'r') as openfile:
    x = [line.rstrip() for line in openfile.readlines()]

# Initialize a dictionary to store counts of each element
opt = {}
# Count each element in `x`
for each in set(x):
    opt[each] = sum([1 for i in x if i == each])

# Print results to user
print(opt)


# EXTRA ============================
# Initialize path to file
# This file has a column of filepaths with a leading '/'
# e.g., '/a/alpha/SUN_sdalfkasjdflka.jpg'
extra_path = 'practice-python/resources/Training_01.txt'

# Open file, read in all lines, and strip the '\n' at the end.
with open(extra_path, 'r') as extra_openfile:
    extra = [line.rstrip() for line in extra_openfile.readlines()]

# Initialize list to store parsed categories
categories = []

# Some categories have subcategories identified by another '/'
for each_path in extra:
    # Remove the leading '/' and parse the files paths
    q = each_path[1:].split('/')

    # If 3 then only 1 category at index 1
    if(len(q) == 3):
       categories.append(q[1])
    # If >3 then grab category and subcategory at index 1 and index 2
    else:
       categories.append("/".join(q[1:3]))


# Initialize a dictionary to store counts of each element
cat_opt = {}
# Count each element in `x`
for each in set(categories):
    cat_opt[each] = sum([1 for i in categories if i == each])

# print results to user
print(cat_opt)
