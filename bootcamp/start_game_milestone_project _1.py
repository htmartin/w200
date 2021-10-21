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


def printBoard_turn():
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
    
print('Tic Tac Toe')
print ('The board looks like this:')
print(printBoard_original())
print("Players take turns placing their mark to try to get three in a row, horizontally,vertically, or diagonally. Let's play!")

#set up so that the program keeps asking for turn input #This works!yay
while True:
p= input('Are you player X or player O? Enter x or o:')
print('Ready Player',p, ". Here's the current state of the game:\n")
print(printBoard_original())
n = int(input('Where do you want to play next? Enter a position number from 1-9 to place your mark?'))
print(printBoard_turn())

#This works!yay
#Where do you want to play next? Enter a position number from 1-9 to place your mark? 9
     |     |   
     |     |      
     |     |   
 ----|-----|----
     |     |   
     |     |      
     |     |   
 ----|-----|----
     |     |   
     |     |  x   
     |     |   
    
    
#It only prints that one move. How to get it to store board?
# add positions to dict? {1:x, 2:o etc}
#write printStoredBoard() function?