# You place a pawn at the top left corner of an n-by-n chess board, labeled (0,0). For each move, you have a choice: move the pawn down a single space, or move the pawn down one space and right one space. That is, if the pawn is at position (i,j), you can move the pawn to (i+1,j) or (i+1, j+1).

# Ask the user for the size of a chessboard, n (integer). Find the number of different paths starting from (0,0) that the pawn could take to reach each position on the chess board. For example, there are two different paths the pawn can take to reach (2,1). Look at the diagrams below to convince yourself of this. You can see the four paths that you can take by move 2.

#   Start -> Move 1 -> Move 2

#   (0,0) ->  (1,0) -> (2,1)

#   (0,0) ->  (1,0) -> (2,0)

#   (0,0) ->  (1,1) -> (2,1)

#   (0,0) ->  (1,1) -> (2,2)
# Print the board with the number of ways to reach each square labeled as shown below.

# For example:

# Enter a board size: 4

# 1 0 0 0
# 1 1 0 0
# 1 2 1 0
# 1 3 3 1
# Please create pseudocode for this problem in the first cell then implement your solution in the second cell.
# If you need help creating pseudocode, read this article: https://www.geeksforgeeks.org/how-to-write-a-pseudo-code/ (code is java but principles are the same)


# #     first row will always be 1 followed by 0s up to the xth spot
# #     second row will always be 1,1 followed by 0s up to the xth spot
    

# Pseudocode Here
""" """given n, The program will allow the user to figure out the number of unique paths to each square of an n x n board """"""

(i,j) is any square, allowable moves are (i+1,j) or (i+1,j+1) 

ask for user_input n = int for n x n board 
if n = x:
    print x rows of x numbers each (each is the number of unique paths to that (i,j) square)
    first number of each row will always be 1
