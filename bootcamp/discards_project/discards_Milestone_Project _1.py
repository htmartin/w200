# def draw_board(a,b,c):
#     '''draws tic tac toe board'''
#     s =  ('\n     |         |')
#     r1 = ('\n    ',a,'    ',b,'   ',c,)
#     #r1 = ('\n __1__ __2__ __3__')
#     r2 = ('\n __4__ __5__ __6__')
#     r3 = ('\n   7     8     9 ')
#     print(s,s,'\n',r1,s,s,r2,s,s, r3)
    
#     def display_board(board):
#     print(board[7]+"|"+board[8]+"|"+board[9])
#     print("-|-|-")
#     print(board[4]+"|"+board[5]+"|"+board[6])
#     print("-|-|-")
#     print(board[1]+"|"+board[2]+"|"+board[3])
#     print("-|-|-")

# testing_board=[" "]*10
# display_board(testing_board)

    
    
#     def draw():
#     # initialize an empty board
#     board = ""

#     # there are 5 rows in a standard tic-tac-toe board
#     for i in range(5):
#         # switch between printing vertical and horizontal bars
#         if i%2 == 0:
#             board += "|    " * 4
#         else:
#             board += " --- " * 3
#         # don't forget to start a new line after each row using "\n"
#         board += "\n"

#     print(board)

# draw()