# 29 Tic Tac Toe Game
# Author: Christian Million
# Started: 2020-08-18
# Completed: 2020-08-18
# Last Modified: 2020-08-18
#
# Prompt: https://www.practicepython.org/exercise/2016/08/03/29-tic-tac-toe-game.html
#
# This exercise is Part 4 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 2, and Part 3.
# 
# In 3 previous exercises, we built up a few components needed to build a Tic Tac Toe game in Python:
# 
# Draw the Tic Tac Toe game board
# Checking whether a game board has a winner
# Handle a player move from user input
# The next step is to put all these three components together to make a two-player Tic Tac Toe game! Your challenge in this exercise is to use the functions from those previous exercises all together in the same program to make a two-player game that you can play with a friend. There are a lot of choices you will have to make when completing this exercise, so you can go as far or as little as you want with it.
# 
# Here are a few things to keep in mind:
# 
# You should keep track of who won - if there is a winner, show a congratulatory message on the screen.
# If there are no more moves left, don’t ask for the next player’s move!
# As a bonus, you can ask the players if they want to play again and keep a running tally of who won more - Player 1 or Player 2.

# This displays a matrix-like board, with a symbol dictionary
def display_board(board, sym):
    for col in board:
        y = ''
        x = ''
        for row in col:
            x = x + ' ---'
            y = y + f'| {sym[row]} '
        print(x)
        print(y + "|")
    print(' ---' * len(board[0]))

# This checkes whether all cells in a row/col/diag are the same
def same(my_list):
    ref = my_list[0]
    for each in my_list:
        if each != ref:
            return False
    return True

# This checks the board for a winner
def check_board(board):
    unlist = [i for each in board for i in each]

    for row in range(0, 7, 3):
        if same(unlist[row:row+3]) and unlist[row] != 0:
            return unlist[row]

    for col in range(3):
        if same(unlist[col:col+6:3]) and unlist[col] != 0:
            return unlist[col]

    if same(unlist[0::4]) or same(unlist[2:8:2]):
        return unlist[4]
    
    else:
        return 0

# Initializes a new game and returns the value of the winner
# 1 = Player 1; 2 = Player 2; 0 = Tie;
def new_game(tokens):

    # Initialize player turn
    player = 0

    # Turn count
    count = 0

    # Initialize empty board
    game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # Display initial board
    display_board(game, tokens)

    # While spaces are available
    while count < 9:
        # Assumer user input is invalid
        valid_input = False

        # increase the game count
        count += 1

        # Switch players
        player = 2 if player == 1 else 1

        # get valid user input
        while not(valid_input):
            # Make sure it comes in the form (2,3)
            try:
                user_input = input(f'Player {player}:\n(provide row,col)\n')
                x = [int(i) for i in user_input.split(',')]
            except:
                print("Remember... Input must be coordinates in {row},{col} coordinates. (e.g., 3,1)")

            # Make sure the integers are valid
            if x[0] not in [1, 2, 3] or x[1] not in [1, 2, 3]:
                print("Rows and columns must be either 1, 2, or 3!")
            # Make sure the spot is empty
            elif game[x[0]-1][x[1]-1] == 0:
                valid_input = True
            # Else it is probably bad input
            else:
                print("Whoa! Looks like that spot is filled up. Try again.")

        # Replace the cell with the players number
        game[x[0]-1][x[1]-1] = player

        # Display the new board
        display_board(game, tokens)

        # Check for a winner
        state = check_board(game)

        # If winner, stop game and return winner
        if(state in [1, 2]):
            print(f'Player {state} wins!')
            return(state)

    # If count gets to 9 and no winner then:        
    print("It's a Tie!")
    return(0)
    print('End of game!')

# Main Method
def main():

    # Initialize tokens
    tokens = {0: " ", 1: "X", 2: "O"}

    # Assume they wanna keep playing
    keep_playing = True

    # Initialize score board
    score = {0: 0, 1: 0, 2: 0}


    print("WELCOME to Tic-Tac-Toe!!!")
    input("Press ENTER when you are ready to play:\n")

    # Allow them to choose their own characters
    if input("Do you want to pick customized tokens for each player?\n").lower()[0] == 'y':
        tokens[1] = input("Player 1, choose your token by entering any character:\n")[0]
        tokens[2] = input("Player 2, choose your token by entering any character:\n")[0]

        if tokens[1] == tokens[2]:
            print("You picked the same tokens which might make it difficult for you to read the board...")

    print("\n\nPerfect! Let's get started!!!")

    # Let them play as many games as they want
    while keep_playing:
        winner = new_game(tokens)
        score[winner] += 1
        print(f'Current Score: Player 1: {score[1]}; Player 2: {score[2]}; Ties: {score[0]};')

        if input("Wanna keep playing?(y/n)\n").lower()[0] == 'n':
            keep_playing = False
        else:
            print("Okay! Let's start!")
    
    print("Well that's it!")
    print(f"The Final Score is: Player 1: {score[1]}; Player 2: {score[2]}; Ties: {score[0]};")
    

if __name__ == '__main__':
    main()
