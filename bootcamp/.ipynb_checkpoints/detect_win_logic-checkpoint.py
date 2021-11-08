# detect win logic

# d = {1:2,2:3}
# print(d[1])


board_dict = {1:1, 2:2, 3:3,4:4, 5:5, 6:6, 7:7, 8:8, 9:9}

board_dict = {1: 'x', 2: 'o', 3: 3, 4: 'x', 5: 'x', 6: 'o', 7: 'o', 8: 8, 9: 'x'}
#stop game if board_dict.values() for keys: (1,2,3) or (4,5,6) or (7,8,9) or (1,4,7) or (1,5,9) or (3,5,7) == 'x' or =='o'
# add to game while loop- 
# if board_dict.values() for keys: (1,2,3) or (4,5,6) or (7,8,9) or (1,4,7) or (1,5,9) or (3,5,7) == 'x' or =='o':
#         break


     |     |   
  x  |  2  |  3   
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
        

        #stop game if board_dict.values() for keys: (1,2,3) or (4,5,6) or (7,8,9) or (1,4,7) or (1,5,9) or (3,5,7) == 'x' or =='o'


#(1,2,3) 
#board_dict = {1:'o', 2:'o', 3:'o',4:4, 5:5, 6:6, 7:7, 8:8, 9:9}

#(4,5,6)
#board_dict = {1:1, 2:2, 3:3,4:'x', 5:'x', 6:'x', 7:7, 8:8, 9:9 }

#(7,8,9)
#board_dict =  {1:1, 2:2, 3:3,4:4, 5:5, 6:6, 7:'o', 8:'o', 9:'o'}

# (1,4,7)
#board_dict = {1:'x', 2:2, 3:3, 4:'x', 5:5, 6:6, 7:'x', 8:8, 9:9}

#(2,5,8)
#board_dict = {1:1, 2:'o', 3:3,4:4, 5:'o', 6:6, 7:7, 8:'o', 9:9}

#(3,6,9)
#board_dict = {1:1, 2:2, 3:'x', 4:4, 5:5, 6:'x', 7:7, 8:8, 9:'x'}

#(3,5,7)
#board_dict = {1:1, 2:2, 3:'o', 4:4, 5:'o', 6:6, 7:'o', 8:8, 9:9}

#(1,5,9)
#board_dict = {1: 'x', 2: 'o', 3: 3, 4: 'x', 5: 'x', 6: 'o', 7: 'o', 8: 8, 9: 'x'}


# add to game while loop- 
# if board_dict.values() for keys: (1,2,3) or (4,5,6) or (7,8,9) or (1,4,7) or (2,5,8) or (3,6,9) or (1,5,9) or (3,5,7) == 'x' or =='o':
#         break




# while True:
#     print('boo')
if board_dict[1] and board_dict[2] and board_dict[3] == 'x' or board_dict[1] and board_dict[2] and board_dict[3]=='o':
    print('boh')
elif board_dict[4] and board_dict[5] and board_dict[6] == 'x' or board_dict[4] and board_dict[5] and board_dict[6]=='o':
    print('baha')
elif board_dict[7] and board_dict[8] and board_dict[9] == 'x' or board_dict[7] and board_dict[8] and board_dict[9] =='o':
    print('bwah')
elif board_dict[1] and board_dict[4] and board_dict[7] == 'x' or board_dict[1] and board_dict[4] and board_dict[7] =='o':  
    print('bwahhaha')
elif board_dict[2] and board_dict[5] and board_dict[8] == 'x' or board_dict[2] and board_dict[5] and board_dict[8] =='o':  
    print('boohoo')
elif board_dict[3] and board_dict[6] and board_dict[9] == 'x' or board_dict[3] and board_dict[6] and board_dict[9] =='o':
    print('woohoo')
elif board_dict[1] and board_dict[5] and board_dict[9] == 'x' or board_dict[1] and board_dict[5] and board_dict[9] =='o':
    print('HaHa')
    
    
# after check simple if then loop(on #(3,6,9)), try-
# while True:
#     print('bah')
#simple if then loop: 
#    break


