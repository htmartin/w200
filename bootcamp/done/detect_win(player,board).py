    
#Run game
while True:
    p= input('Are you player X or player O? Enter x or o:')
    n = int(input('Ready Player. Where do you want to play next? Enter a position number from 1-9 to place your mark?'))
    board_dict[n]= p
    #updates board_dict with appropriate n:p pair before we call printBoard
    print(printBoard_original())

def detect_win(player,board):
    if board[1] and board[2] and board[3] == p:
        print(p, 'wins')
        break
    

    detect_win(p,board_dict)
    
    

if board_dict[1] and board_dict[2] and board_dict[3] == 'x':
        print('X wins')
        break
    
    elif board_dict[1] and board_dict[2] and board_dict[3]=='o':
        print('O wins')
        break