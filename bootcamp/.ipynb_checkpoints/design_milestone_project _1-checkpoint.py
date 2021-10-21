# Overall design
# - Tell players what to do (game instructions) with (printBoard_original()) - board with 1-9 positions shown
# - Print the current state of the board when asking for input for each move Here's the current state of the game: #How to print actual state?
# - √move input
# - Correct their input when needed(deal with this once basic game play is working)
# √ Print current state of the board 
# - after each move
# - store the current state of the board as turns go on
# - determine when one player wins 
# - (end game messaging)


def printBoard_original():   
    board = [x for x in range(10)] #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print ( "     |     |   ")
    print (" ",board[1]," | ", board[2], " | ", board[3],"  ")
    print ( "     |     |   ")
    print (" ----|-----|----")
    print ( "     |     |   ")
    print (" ",board[4]," | ", board[5], " | ", board[6],"  ")
    print ( "     |     |   ")
    print (" ----|-----|----")
    print ( "     |     |   ")
    print (" ",board[7]," | ", board[8], " | ", board[9],"  ")
    print ( "     |     |   ")
    print ("     |     |   ")

    
printBoard_original() gives
     |     |   
  1  |  2  |  3   
     |     |   
 ----|-----|----
     |     |   
  4  |  5  |  6   
     |     |   
 ----|-----|----
     |     |   
  7  |  8  |  9   
     |     |   
     |     |   
    
    
def printBoard_turn():
    n = 3 
    p = 'o' 
    board = [x for x in range(10)] #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
    #want board = [' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' ']
    for i in board:
        if i == n:
            board[i]=p
        else:
            board[i]=' '

    print ( "     |     |   ")
    print (" ",board[1]," | ", board[2], " | ", board[3],"  ")
    print ( "     |     |   ")
    print (" ----|-----|----")
    print ( "     |     |   ")
    print (" ",board[4]," | ", board[5], " | ", board[6],"  ")
    print ( "     |     |   ")
    print (" ----|-----|----")
    print ( "     |     |   ")
    print (" ",board[7]," | ", board[8], " | ", board[9],"  ")
    print ( "     |     |   ")
    

    

def turn_input():
    p= input('Are you player X or player O? Enter x or o:')
    print('Ready Player',p, ". Here's the current state of the game:\n")
    printBoard_turn()
    n = int(input('Where do you want to play next? Enter a position number from 1-9 to place your mark?'))
    return n
    return p
 



# working on: Print current state of the board: 
#Where do you want to play next? Enter a position number from 1-9 to place your mark? 6

#(still in move_input_milestone_project _1.py)