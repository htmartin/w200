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


# OK now I think I just need
# - detect win logic
# - input correction
refactor_whole_game_milestone_project1