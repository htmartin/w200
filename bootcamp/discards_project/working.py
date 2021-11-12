board_dict = {1:'x', 2:'o', 3:3,4:4, 5:5, 6:6, 7:7, 8:8, 9:9}
#leave as dict - how to print vaslues based on keys???
board_list = list(board_dict.values())
print(board_list)

#It prints the board fine with board_list = ['x', 'o', 3, 4, 5, 6, 7, 8, 9]
#It's trying to change the list that's barfing
for i in board_list:
    if i == n:
        board_list[i]=p
    else:
        board_list[i]=''
        
['x', 'o', 3, 4, 5, 6, 7, 8, 9]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-15-2a129afb4a06> in <module>
     10         board_list[i]=p
     11     else:
---> 12         board_list[i]=''

TypeError: list indices must be integers or slices, not str

    
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

     |     |   
  x  |  o  |  3   
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