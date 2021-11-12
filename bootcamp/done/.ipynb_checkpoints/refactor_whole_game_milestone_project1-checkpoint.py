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
    
#Instructions   
print('Tic Tac Toe')
print ('The board looks like this:')
print(printBoard_original())
print("Players take turns placing their mark to try to get three \
in a row, horizontally,vertically, or diagonally. Let's play!")



#Run game
while True:
    p= input('Are you player X or player O? Enter x or o:')
    n = int(input('Ready Player. Where do you want to play next? Enter a position number from 1-9 to place your mark?'))
    board_dict[n]= p
    #updates board_dict with appropriate n:p pair before we call printBoard
    print(printBoard_original())
    if board_dict[1] == 'x' and board_dict[2] == 'x' and board_dict[3] == 'x':
        print('X wins')
        break
    elif board_dict[1] == 'o' and board_dict[2] == 'o' and board_dict[3]=='o':
        print('O wins')
        break

    elif board_dict[4]== 'x' and board_dict[5] == 'x' and board_dict[6] == 'x':
        print('X wins')
        break

    elif board_dict[4] == 'o' and board_dict[5] == 'o' and board_dict[6]=='o':
        print('O wins')
        break

    elif board_dict[7] == 'x' and board_dict[8] == 'x' and board_dict[9] == 'x':
        print('X wins')
        break

    elif board_dict[7] == 'o' and board_dict[8] == 'o' and board_dict[9] =='o':
        print('O wins')
        break

    elif board_dict[1] == 'x' and board_dict[4] == 'x' and board_dict[7] == 'x':
        print('X wins')
        break

    elif board_dict[1] == 'o' and board_dict[4] == 'o' and board_dict[7] =='o':  
        print('O wins')
        break

    elif board_dict[2] == 'x' and board_dict[5] == 'x' and board_dict[8] == 'x':
        print('X wins')
        break

    elif board_dict[2] == 'o' and board_dict[5] == 'o' and board_dict[8] =='o':  
        print('O wins')
        break

    elif board_dict[3] == 'x' and board_dict[6] == 'x' and board_dict[9] == 'x':
        print('X wins')
        break

    elif board_dict[3] == 'o' and board_dict[6] == 'o' and board_dict[9] =='o':
        print('O wins')
        break

    elif board_dict[1] == 'x' and board_dict[5] == 'x' and board_dict[9] == 'x':
        print('X wins')
        break

    elif board_dict[3] == 'o' and board_dict[5] =='o' and board_dict[7] =='o':
        print('O wins')
        break


# OK now I think I just need
# - input correction
refactor_whole_game_milestone_project1