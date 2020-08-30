# 27 Tic Tac Toe Draw
# Author: Christian Million
# Started: 2020-08-18
# Completed: 2020-08-18
# Last Modified: 2020-08-18
#
# Prompt: https://www.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html
#
# This exercise is Part 3 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 2, and Part 4.
# 
# In a previous exercise we explored the idea of using a list of lists as a “data structure” to store information about a tic tac toe game.
# In a tic tac toe game, the “game server” needs to know where the Xs and Os are in the board, to know whether player 1 or player 2 (or whoever is X and O won).
# 
# There has also been an exercise about drawing the actual tic tac toe gameboard using text characters.
# 
# The next logical step is to deal with handling user input. When a player (say player 1, who is X)
# wants to place an X on the screen, they can’t just click on a terminal.
# So we are going to approximate this clicking simply by asking the user for a coordinate of where they want to place their piece.
# 
# As a reminder, our tic tac toe game is really a list of lists. The game starts out with an empty game board like this:
# 
# game = [[0, 0, 0],
# 	[0, 0, 0],
# 	[0, 0, 0]]
# The computer asks Player 1 (X) what their move is (in the format row,col), and say they type 1,3. Then the game would print out
# 
# game = [[0, 0, X],
# 	[0, 0, 0],
# 	[0, 0, 0]]
# And ask Player 2 for their move, printing an O in that place.
# 
# Things to note:
# 
# For this exercise, assume that player 1 (the first player to move) will always be X and player 2 (the second player) will always be O.
# Notice how in the example I gave coordinates for where I want to move starting from (1, 1) instead of (0, 0).
# To people who don’t program, starting to count at 0 is a strange concept, so it is better for the user experience if the row counts and column counts start at 1.
# This is not required, but whichever way you choose to implement this, it should be explained to the player.
# Ask the user to enter coordinates in the form “row,col” - a number, then a comma, then a number.
# Then you can use your Python skills to figure out which row and column they want their piece to be in.
# Don’t worry about checking whether someone won the game, but if a player tries to put a piece in a game position where there already is another piece, do not allow the piece to go there.
# Bonus:
# 
# For the “standard” exercise, don’t worry about “ending” the game - no need to keep track of how many squares are full.
# In a bonus version, keep track of how many squares are full and automatically stop asking for moves when there are no more valid moves.

# Create symbols for each player
sym = {1: "X", 2: "O"}

# Initialize an empty game
game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

# Indicates whos turn it is
player = 0

# Indicates whether the game is still being played
playing = True

# Counts the number of turns taken
count = 0

while count < 9:
    # Get valid input from user
    valid_input = False
    count += 1
    player = 2 if player == 1 else 1
    

    while not(valid_input):
        try:
            # User input should be e.g., '2,3'
            user_input = input('Coordinates:\n')

            # Splits user input into list
            x = [int(i) for i in user_input.split(',')]
            
            # Check to make user number is valid
            if x[0] not in [1, 2, 3] or x[1] not in [1, 2, 3]:
                print("Rows and columns must be either 1, 2, or 3!")

            # Make sure a spot is available
            elif game[x[0]-1][x[1]-1] == 0:
                valid_input = True

            else:
                print("Whoa! Looks like that spot is filled up. Try again.")
        except:
            print("Remember... Input must be coordinates in {row},{col} coordinates. (e.g., 3,1)")

    # Once input is valid, replace their coordinates with the symbol
    game[x[0]-1][x[1]-1] = sym[player]

    # Check For Winner would be Here
        
    print(game)

# End the game
print(f'End of game: {game}')