# Overall design
# - Tell players what to do (game instructions)
# - move messaging 
# - move input
# - Correct their input when needed
# - print the board for each move
# - determine when one player wins


##Print board 


#def draw_board(a,b,c,d,e,f,g,h,i):


#input will be a number for position bt 1-9. 
#1.How to print board based on one turn's input?
#2.How to print board based on one turn's input
#plus the history of prior moves (current state of the board)?
#3.How to store current state of the board?
    

 #Print board at all:      

board = [x for x in range(10)] #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

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
p = 'o' # player is x or o
board = [x for x in range(10)] #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def printBoard():
    for i in board:
        if i == n:
            i = p
        else i == ' '
            
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
o
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
        
#how to iterate over board[#s]in print list?