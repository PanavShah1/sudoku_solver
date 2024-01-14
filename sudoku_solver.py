sudoku = [
    [8, 0, 6, 0, 1, 0, 0, 0, 0],
    [0, 0, 3, 0, 6, 4, 0, 9, 0],
    [9, 0, 0, 0, 0, 0, 8, 1, 6],
    [0, 8, 0, 3, 9, 6, 0, 0, 0],
    [7, 0, 2, 0, 4, 0, 3, 0, 9],
    [0, 0, 0, 5, 7, 2, 0, 8, 0],
    [5, 2, 1, 0, 0, 0, 0, 0, 4],
    [0, 3, 0, 7, 5, 0, 2, 0, 0],
    [0, 0, 0, 0, 2, 0, 1, 0, 5]
]

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
def check_box(rs, re, cs, ce):
    for i in range(rs, re+1):
        for ii in range(cs, ce+1):
            if len(possible_values[9*i+ii])==1:
                value = sudoku[i][ii]
                # print(value)
                for iii in range(rs, re+1):
                    for iv in range(cs, ce+1):
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

    check_box(0, 2, 0, 2)
    check_box(0, 2, 3, 5)
    check_box(0, 2, 6, 8)
    check_box(3, 5, 0, 2)
    check_box(3, 5, 3, 5)
    check_box(3, 5, 6, 8)
    check_box(6, 8, 0, 2)
    check_box(6, 8, 3, 5)
    check_box(6, 8, 6, 8)

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

        



ctr = 0
while ctr<81:
    ctr = 0
    for element in possible_values:
        if len(element)==1:
            ctr+=1
    loop_through()
    
    






    

