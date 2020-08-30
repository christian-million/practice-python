# 26 Check Tic Tac Toe
# Author: Christian Million
# Started: 2020-08-18
# Completed: 2020-08-18
# Last Modified: 2020-08-18
#
# Prompt: https://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html
#
# This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 3, and Part 4.
# 
# As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, this is significantly more than half an hour of coding, so we’re doing it in pieces.
# 
# Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.
# 
# If a game of Tic Tac Toe is represented as a list of lists, like so:
# 
# game = [[1, 2, 0],
# 	     [2, 1, 0],
# 	     [2, 1, 1]]
# where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.
# 
# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal.
# Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.
# 
# Here are some more examples to work with:

winner_is_2 = [[2, 2, 0],
	           [2, 1, 0],
	           [2, 1, 1]]

winner_is_1b = [[2, 2, 0],
	           [0, 1, 0],
	           [1, 1, 1]]

winner_is_1 = [[1, 2, 0],
	            [2, 1, 0],
	            [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
                   [2, 1, 0],
	                 [2, 1, 1]]

no_winner = [[1, 2, 0],
	            [2, 1, 0],
	            [2, 1, 2]]

also_no_winner = [[1, 2, 0],
	                [2, 1, 0],
	                [2, 1, 0]]


# Create a function that tests whether all elements a row are the same.
# Could've used the all() function but whatevs
def same(my_list):
    ref = my_list[0]
    for each in my_list:
        if each != ref:
            return False
    return True

# Check matrix for a winner
def check_board(board):
    # Unlist the matrix so we can traverse a single list
    unlist = [i for each in board for i in each]

    # For each row, check to see if all 3 are same and not 0 (blanks)
    for row in range(0, 7, 3):
        if same(unlist[row:row+3]) and unlist[row] != 0:
            return unlist[row]

    # For each column, check to see if all 3 are same and not 0
    for col in range(3):
        if same(unlist[col:col+6:3]) and unlist[col] != 0:
            return unlist[col]

    # Check the diagnals
    if same(unlist[0::4]) or same(unlist[2:8:2]):
        return unlist[4]
    
    else:
        return 0


print(check_board(winner_is_1))
print(check_board(winner_is_2))
print(check_board(winner_is_also_1))
print(check_board(winner_is_1b))
print(check_board(no_winner))
print(check_board(also_no_winner))