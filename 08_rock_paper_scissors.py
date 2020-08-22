# 08 Rock Paper Scissors
# Author: Christian Million
# Started: 2020-08-21
# Completed: 2020-08-21
# Last Modified: 2020-08-22
#
# Prompt: https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
#
# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of
# congratulations to the winner, and ask if the players want to start a new game)
# 
# Remember the rules:
# 
# - Rock beats scissors
# - Scissors beats paper
# - Paper beats rock

# Inititalize
end = False
validMoves = ['p', 'r', 's']

# Coninue playing until they say no.
while not(end):

    # Initialize valid move flags
    validP1 = False
    validP2 = False

    # Make sure move is valid before continuing...
    while not(validP1):
        p1 = input("Player 1: Rock(r), Paper(p), or Scissors(s)?\n").lower()[0]
        validP1 = p1 in validMoves
        if(not(validP1)):
            print("WHOA - NOT VALID MOVE - TRY AGAIN PLAYER 1")

    # Make sure move is valid before continuing
    while not(validP2):
        p2 = input("Player 2: Rock(r), Paper(p), or Scissors(s)?\n").lower()[0]
        validP2 = p2 in validMoves
        if(not(validP2)):
            print("WHOA - NOT VALID MOVE - TRY AGAIN PLAYER 2")

    # Check if Tie or Player 1 Wins, else it is Player 2
    if(p1 == p2):
        winner = 'Tie'
    elif(p1 == 'p' and p2 == 'r'):
        winner = 'Player 1'
    elif(p1 == 'r' and p2 == 's'):
        winner = 'Player 1'
    elif(p1 == 's' and p2 == 'p'):
        winner = 'Player 1'
    else:
        winner = 'Player 2'

    # If tie, start the while loop again
    if(winner == 'Tie'):
        print("Draw! Try again.")
    # Else ask for another game
    else:
        print(f'Winner is {winner}.')
        again = input("Would you like to play again?(y/n)\n").lower()[0]
        if(again == 'n'):
            end = True

# Farewell!
print('Goodbye!!')