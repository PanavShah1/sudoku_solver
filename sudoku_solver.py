import copy


original_sudoku = [
    [3, 0, 0, 0, 0, 0, 0, 0, 0],
    [6, 5, 0, 0, 1, 0, 0, 7, 0],
    [0, 0, 4, 2, 0, 7, 5, 0, 0],
    [0, 0, 0, 9, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 0, 0, 0, 0, 9],
    [0, 9, 0, 0, 6, 3, 0, 4, 2],
    [1, 7, 5, 0, 3, 0, 0, 6, 4],
    [0, 4, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 8, 0, 0, 0, 0, 0, 0]
]


sudoku = copy.deepcopy(original_sudoku)


notsolved = True

# val = column*9 + row
# n = 9*i+j

possible_values = [[] for i in range(81)]

for i in range(81):
    possible_values[i] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(possible_values)
    
for i in range(9):
    for j in range(9):
        if sudoku[i][j]!=0:
            possible_values[9*i+j] = [sudoku[i][j]]

# print(possible_values)
            
# Checking numbers in the boxes
def check_box(rs, cs):
    for i in range(rs, rs+3):
        for ii in range(cs, cs+3):
            if len(possible_values[9*i+ii])==1:
                value = sudoku[i][ii]
                # print(value)
                for iii in range(rs, rs+3):
                    for iv in range(cs, cs+3):
                        if len(possible_values[9*iii+iv])!=1:
                            if value in possible_values[9*iii+iv]:
                                possible_values[9*iii+iv].remove(value)
                                if len(possible_values[9*iii+iv])==1:
                                    sudoku[iii][iv]=possible_values[9*iii+iv][0]
                                    print('hi')
                            # else:
                            #     print(f"Value {value} not in list, cannot remove.")

def check_row(i):
    for ii in range(0, 9):
        if len(possible_values[9*i+ii]) == 1:
            value = sudoku[i][ii]
            # print(value)
            for iii in range(0, 9):
                if len(possible_values[9*i+iii])!=1:
                    if value in possible_values[9*i+iii]:
                        possible_values[9*i+iii].remove(value)
                        if len(possible_values[9*i+iii])==1:
                            sudoku[i][iii]=possible_values[9*i+iii][0]
                            print('hi')

                    # else:
                    #     print(f"Value {value} not in list, cannot remove.")

def check_column(ii):
    for i in range(0, 9):
        if len(possible_values[9*i+ii]) == 1:
            value = sudoku[i][ii]
            # print(value)
            for iii in range(0, 9):
                if len(possible_values[9*iii+ii])!=1:
                    if value in possible_values[9*iii+ii]:
                        possible_values[9*iii+ii].remove(value)
                        if len(possible_values[9*iii+ii])==1:
                            sudoku[iii][ii]=possible_values[9*iii+ii][0]
                            print('hi')

                    # else:
                    #     print(f"Value {value} not in list, cannot remove.")
            

def loop_through():

    check_box(0, 0)
    check_box(0, 3)
    check_box(0, 6)
    check_box(3, 0)
    check_box(3, 3)
    check_box(3, 6)
    check_box(6, 0)
    check_box(6, 3)
    check_box(6, 6)

    # for i in range(0, 9):
    #     for j in range(0, 9):
    #         print(f'{i}, {j} : {possible_values[9*i+j]}')

    check_row(0)
    check_row(1)
    check_row(2)
    check_row(3)
    check_row(4)
    check_row(5)
    check_row(6)
    check_row(7)
    check_row(8)

    # for i in range(0, 9):
    #     for j in range(0, 9):
    #         print(f'{i}, {j} : {possible_values[9*i+j]}')

    check_column(0)
    check_column(1)
    check_column(2)
    check_column(3)
    check_column(4)
    check_column(5)
    check_column(6)
    check_column(7)
    check_column(8)

    for i in range(0, 9):
        for j in range(0, 9):
            print(f'{i}, {j} : {possible_values[9*i+j]}')

    print()
    print()








def valid_box(rs, cs, num):
    ctr = 0
    for i in range(rs, rs+3):
        for j in range(cs, cs+3):
            if sudoku[i][j] == num:
                ctr+=1
    if ctr>1:
        print('not valid')
        return False
    else:
        return True

   
def valid_row(r, num):
    ctr = 0
    for i in range(0, 9):
        if sudoku[r][i] == num:
            ctr+=1
    if ctr>1:
        print('not valid')
        return False
    else: 
        return True

def valid_column(c, num):
    ctr = 0
    for i in range(0, 9):
        if sudoku[i][c] == num:
            ctr+=1
    if ctr>1:
        print('not valid')
        return False
    else:
        return True

def valid_sudoku():

    ctr = 0
    for i in range(1, 10):
        if valid_box(0, 3, i) and valid_box(0, 0, i) and valid_box(0, 6, i) and valid_box(3, 0, i) and valid_box(3, 3, i) and valid_box(3, 6, i) and valid_box(6, 0, i) and valid_box(6, 3, i) and valid_box(6, 6, i) and valid_row(0, i) and valid_row(1, i) and valid_row(2, i) and valid_row(3, i) and valid_row(4, i) and valid_row(5, i) and valid_row(6, i) and valid_row(7, i) and valid_row(8, i) and valid_column(0, i) and valid_column(1, i) and valid_column(2, i) and valid_column(3, i) and valid_column(4, i) and valid_column(5, i) and valid_column(6, i) and valid_column(7, i) and valid_column(8, i):
            pass
        else:
            # print("Nope not valid")
            ctr+=1
    print(f'ctr = {ctr}')






while True:
    old = copy.deepcopy(sudoku)
    loop_through()
    # valid_sudoku()
    if sudoku==old:
        break


print('manipulation')
sudoku[2][4] = 9 #9
possible_values[2*9+4] = [9]
while True:
    old = copy.deepcopy(sudoku)
    loop_through()
    valid_sudoku()
    if sudoku==old:
        break

# valid_sudoku()

# print('manipulation 2')
# sudoku[8][5] = 8
# possible_values[77] = [8]
# while True:
#     old = copy.deepcopy(sudoku)
#     loop_through()
#     # valid_sudoku()
#     if sudoku==old:
#         break

# valid_sudoku()

# print('manipulation 3')
# sudoku[8][1] = 3
# possible_values[73] = [3]
# while True:
#     old = copy.deepcopy(sudoku)
#     loop_through()
#     # valid_sudoku()
#     if sudoku==old:
#         break

# valid_sudoku()



    





print("Original Sudoku")
for i in range(9):
    print(original_sudoku[i])

print()

print("Solved Sudoku")
for i in range(9):
    print(sudoku[i])
    






    

