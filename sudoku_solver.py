import copy


original_sudoku = [
    [0, 0, 7, 0, 0, 0, 8, 2, 0],
    [0, 9, 0, 0, 0, 1, 0, 0, 0],
    [0, 4, 0, 9, 7, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 4, 0, 6],
    [0, 0, 3, 0, 0, 0, 7, 0, 0],
    [5, 0, 6, 7, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 4, 0, 5, 0],
    [0, 0, 0, 6, 0, 0, 0, 1, 0],
    [0, 2, 4, 0, 0, 0, 6, 0, 0]
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

    # for i in range(0, 9):
    #     for j in range(0, 9):
    #         print(f'{i}, {j} : {possible_values[9*i+j]}')

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
        if valid_box(0, 0, i) and valid_box(0, 3, i) and valid_box(0, 6, i) and valid_box(3, 0, i) and valid_box(3, 3, i) and valid_box(3, 6, i) and valid_box(6, 0, i) and valid_box(6, 3, i) and valid_box(6, 6, i) and valid_row(0, i) and valid_row(1, i) and valid_row(2, i) and valid_row(3, i) and valid_row(4, i) and valid_row(5, i) and valid_row(6, i) and valid_row(7, i) and valid_row(8, i) and valid_column(0, i) and valid_column(1, i) and valid_column(2, i) and valid_column(3, i) and valid_column(4, i) and valid_column(5, i) and valid_column(6, i) and valid_column(7, i) and valid_column(8, i):
            pass
        else:
            # print("Nope not valid")
            ctr+=1
    print(f'ctr = {ctr}')
    if ctr == 0:
        return True
    else:
        return False
    
def all_full():
    ctr = 0
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]==0:
                ctr+=1
    if(ctr>0):
        return False
    else:
        return True

def try_solving():
    while True:
        old = copy.deepcopy(sudoku)
        loop_through()
        valid_sudoku()
        if sudoku==old:
            break

    # print("Original Sudoku")
    # for i in range(9):
    #     print(original_sudoku[i])

    print()

    print("Solved Sudoku")
    for i in range(9):
        print(sudoku[i])

try_solving()


def try_cases(num, length):
    history = []
    assumed_value = 0
    flag = False
    global possible_values
    global sudoku
    for i in range(0, 9):
        for ii in range(0,9):
            if len(possible_values[9*i+ii])==length:
                assumed_value = possible_values[9*i+ii][num]
                history = [copy.deepcopy(sudoku), copy.deepcopy(possible_values), i, ii, assumed_value]
                print(f'history = {history}')
                sudoku[i][ii] = assumed_value
                possible_values[9*i+ii]=[assumed_value]
                try_solving()

                if valid_sudoku() and all_full():     
                    flag = True
                    print(f'valid_sudoku = {valid_sudoku()} + all_full = {all_full()} + flag = True')
                else:
                    sudoku = history[0]
                    possible_values = history[1]
                    print(f'valid_sudoku = {valid_sudoku()} + all_full = {all_full()} + flag = False')
                print(f'sudoku = {sudoku}')
            if flag == True:
                break
        if flag == True:
            break

    try_solving()

    print("NEEDED")
    print(f'history = {history[0]}\n{history[1]}\n{history[2]}\n{history[3]}\n{history[4]}')




print('guess')
if not valid_sudoku() or not all_full():
    print('0, 2')
    try_cases(0, 2)

if not valid_sudoku() or not all_full():
    print('1, 2')
    try_cases(1, 2)

if not valid_sudoku() or not all_full():
    print('0, 3')
    try_cases(0, 3)

if not valid_sudoku() or not all_full():
    print('1, 3')
    try_cases(1, 3)

if not valid_sudoku() or not all_full():
    print('2, 3')
    try_cases(2, 3)








            





    



    






    

