board_dict = {1:1, 2:2, 3:3,4:4, 5:5, 6:6, 7:7, 8:8, 9:9}

def printBoard_original():   
    board_list = list(board_dict.values())
    
    print ( "     |     |   ")
    print (" ",board_list[0]," | ", board_list[1], " | ", board_list[2],"  ")
    print ( "     |     |   ")
    print (" ----|-----|----")
    print ( "     |     |   ")
    print (" ",board_list[3]," | ", board_list[4], " | ", board_list[5],"  ")
    print ( "     |     |   ")
    print (" ----|-----|----")
    print ( "     |     |   ")
    print (" ",board_list[6]," | ", board_list[7], " | ", board_list[8],"  ")
    print ( "     |     |   ")
    print ("     |     |   ")
    
    
#get printBoard turn to update board_dict
def printBoard_turn():
    board_list = list(board_dict.values())
    print(board_list)
    for i in board_list:
        if i == n:
            board_list[i]=p
        else:
            board_list[i]=' '

    print ( "     |     |   ")
    print (" ",board_list[0]," | ", board_list[1], " | ", board_list[2],"  ")
    print ( "     |     |   ")
    print (" ----|-----|----")
    print ( "     |     |   ")
    print (" ",board_list[3]," | ", board_list[4], " | ", board_list[5],"  ")
    print ( "     |     |   ")
    print (" ----|-----|----")
    print ( "     |     |   ")
    print (" ",board_list[6]," | ", board_list[7], " | ", board_list[8],"  ")
    print ( "     |     |   ")
    print ("     |     |   ")
    
#Instructions   
print('Tic Tac Toe')
print ('The board looks like this:')
print(printBoard_original())
print("Players take turns placing their mark to try to get three \
in a row, horizontally,vertically, or diagonally. Let's play!")
n = 3


#Run game
while True:
    p= input('Are you player X or player O? Enter x or o:')
    print('Ready Player',p, ". Here's the current state of the game:\n")
    print(printBoard_turn())
    n = int(input('Where do you want to play next? Enter a position number from 1-9 to         place your mark?'))
    board_dict[n]= p
    #update board_dict with appropriate n:p pair before we call printBoard_turn
print(printBoard_turn())
#Integrate update board_dict back in with functions 
#so printing board matching board_dict each move


Get
Tic Tac Toe
The board looks like this:
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
None
Players take turns placing their mark to try to get three in a row, horizontally,vertically, or diagonally. Let's play!
Are you player X or player O? Enter x or o: x
Ready Player x . Here's the current state of the game:

[1, 2, 3, 4, 5, 6, 7, 8, 9]
---> 10     print(printBoard_turn())
----> 9             board_list[i]=' '
Then TypeError: list indices must be integers or slices, not str
