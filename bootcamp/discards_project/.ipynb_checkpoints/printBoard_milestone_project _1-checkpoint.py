# - Print the board for each move

#def draw_board(a,b,c,d,e,f,g,h,i):


#input will be a number for position bt 1-9. 
#1.How to print board based on one turn's input?
#2.How to print board based on one turn's input
#plus the history of prior moves (current state of the board)?
#3.How to store current state of the board?
    

 #Print board at all:      

board = [x for x in range(10)] #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

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
 

printBoard() gives
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

#1.How to print board based on one turn's input?
#loop over printBoard()?
#can you loop over a func?

n = 3 #input will be a number for position bt 1-9. 
p = 'x' # input will be player is x or o
board = [x for x in range(10)] #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# want: board = [' ', ' ', ' ', x, ' ', ' ', ' ', ' ', ' ']

# If board = [' ', ' ', ' ', x, ' ', ' ', ' ', ' ', ' ']
#Then 
def printBoard():
   
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
    print ("      |     |   ")
 
printBoard() gives

     |     |   
     |     |  x   
     |     |   
 ----|-----|----
     |     |   
     |     |      
     |     |   
 ----|-----|----
     |     |   
        
# How to get? board = [' ', ' ', ' ', x, ' ', ' ', ' ', ' ', ' ']

board = [x for x in range(10)] #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
#want board = [' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ']
for i in board:
    if i == n:
        board[i]=p
    else:
        board[i]=' '
print(board)

#get: [' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' ', ' ']

#Put it back with def printBoard():

n = 3 #input will be a number for position bt 1-9. 
p = 'o' # input will be player is x or o
board = [x for x in range(10)] #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
#want board = [' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' ']
for i in board:
    if i == n:
        board[i]=p
    else:
        board[i]=' '


def printBoard():
   
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
    

    
#Get inputs to play with printBoard() work