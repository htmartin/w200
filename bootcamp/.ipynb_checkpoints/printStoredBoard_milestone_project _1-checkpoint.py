#It only prints that one move. How to get it to store board?
# add positions to dict? {1:x, 2:o etc}
#write printStoredBoard() function?
#original positions in board_dict = {1:'1', 2:2,}
#get printBoard turn to update board_dict


board_dict = {1:1, 2:2, 3:3,4:4, 5:5, 6:6, 7:7, 8:8, 9:9}

def printBoard_original():   
    board_list = list(board_dict.values())
    print(board_list)
    
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
    
    
while True:
p= input('Are you player X or player O? Enter x or o:')
print('Ready Player',p, ". Here's the current state of the game:\n")
print(printBoard_original())
n = int(input('Where do you want to play next? Enter a position number from 1-9 to place your mark?'))
#update board_dict with appropriate n:p pair before we call printBoard_turn
print(printBoard_turn())