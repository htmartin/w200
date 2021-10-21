

# before this will be - Tell players what to do (game instructions)    

# - Print the current state of the board when asking for input for each move Here's the current state of the game: #How to print actual state?
    #√Get inputs to play with printBoard() work
# - store the current state of the board as turns go on

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
 

 turn_input() gives

Are you player X or player O? Enter x or o: o
Ready Player o . Here's the current state of the game: #How to print actual state?

     |     |   
     |     |  o   
     |     |   
 ----|-----|----
     |     |   
     |     |      
     |     |   
 ----|-----|----
     |     |   
     |     |      
     |     |   
Where do you want to play next? Enter a position number from 1-9 to place your mark? 6
6
# working on: Print current state of the board: 
#Where do you want to play next? Enter a position number from 1-9 to place your mark? 6

#(still in move_input_milestone_project _1.py)