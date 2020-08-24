# 24 Draw A Game Board
# Author: Christian Million
# Started: 2020-08-23
# Completed: 2020-08-23
# Last Modified: 2020-08-24
#
# Prompt: https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html
#
# This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.
# 
# Time for some fake graphics! Let’s say we want to draw game boards that look like this:
# 
#  --- --- --- 
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- --- 
# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).
# 
# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
# 
# Remember that in Python 3, printing to the screen is accomplished by
# 
#   print("Thing to show on screen")
# Hint: this requires some use of functions, as were discussed previously on this blog and elsewhere on the Internet, like this TutorialsPoint link.

# NOTE TO SELF:
# I think the printCol and printRow functions can be collapsed even further.
# Also, consider how you would want to put objects between |   |

# Initialize example game board dimensions
ROWS = 4
COLS = 5

# Define a function to pad a string with symbols
def pad(str, sym = " "):
    return sym + str + sym

# Function that prints the initial row of columns
def printCol(cols):
    print(pad(" ".join(["---"] * cols)))
    print(pad("|".join(["   "] * cols), "|"))
    print(pad(" ".join(["---"] * cols)))

# Function that adds rows
def printRows(cols):
    print(pad("|".join(["   "] * cols), "|"))
    print(pad(" ".join(["---"] * cols)))

# Combines functions above to print board
def printBoard(cols, rows):
    printCol(cols)
    for i in range(rows-1):
        printRows(cols)

# Return board to user
printBoard(COLS, ROWS)