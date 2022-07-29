import copy

def showSquare(square_in):
    for row in square_in:
        for n in row:
            print(n, end=' ')
        print()

def getUsedValues(square_in, r, c):
    #used values in row
    values_in_row = []

    for i in range(9):
        if square[r][i] != 0:
            values_in_row += [square[r][i]]

    # used values in column
    values_in_col = []

    for i in range(9):
        if square[i][c] != 0:
            values_in_col += [square[i][c]]

    #used values in box

    values_in_box = []

    startrow = 3 * (r // 3)

    startcol =  3 * (c // 3)
    
    for j in range(3):
        for n in range(3):

            value = square[startrow + j][startcol + n]

            if value != 0:

                values_in_box += [value]

    all_used_values = set(values_in_row + values_in_col + values_in_box)

    return all_used_values

def guessValue(square_in, r, c, current_number_in):
    all_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    x = all_values.index(current_number_in) + 1

    del all_values[0:x]

    set_all_greater_values = set(all_values)
    
    used = getUsedValues(square_in, r, c)

    s = set_all_greater_values.difference(used)

    unused = list(s)
    
    if len(unused) > 0:

        unused.sort()

        guess = unused[0]

    else:
        
        guess = None

    #print('Guess: {}'.format(guess))

    return guess

## square = [1, 0, 0, 0, 7, 0, 0, 0, 2],
##          [0, 7, 0, 0, 0, 0, 0, 5, 0],
##          [0, 0, 5, 2, 3, 8, 7, 0, 0],
##          [0, 0, 7, 0, 0, 0, 2, 0, 0],
##          [0, 0, 9, 1, 2, 5, 6, 0, 0],
##          [0, 0, 6, 0, 0, 0, 1, 0, 0],
##          [0, 0, 4, 7, 8, 6, 3, 0, 0],
##          [0, 6, 0, 0, 0, 0, 0, 4, 0],
##          [2, 0, 0, 0, 4, 0, 0, 0, 6]

square = []

print('Enter your incomplete square, line by line below:')
for i in range(9):
    while True:
        line = input('Line {}: '.format(i + 1))
        line_list = []
        
        if len(line) == 9:
            for ch in line:
                if ch in '1234567890':
                    ch = int(ch) 
                    line_list += [ch]
                
                else:
                    print('Invalid Input: input only numbers')
                    pass

            square += [line_list]
            break

        else:
            print('Invalid Length: input 9 numbers')



stack = []

row = 0
col = 0

while row < 9:

    col = 0

    while col < 9:

        if square[row][col] == 0:

            while True:

                current_value = square[row][col]

                guess = guessValue(square, row, col, current_value)

                if guess != None:                
                    
                    square[row][col] = guess

                    stack += [{'square':copy.deepcopy(square), 'row': row, 'col': col}]

                    break
                 
                else:

                    snapshot = stack[-1]

                    square = snapshot['square']

                    row = snapshot['row']

                    col = snapshot['col']

                    stack.pop(-1)
                           
        col += 1

    row += 1

for line in square:
    if 0 not in line:
        print('\nSolved:')
        showSquare(square)
    else:
        print('\nNot Solvable')

####Recursive Sudoku Solver
##def display(square_in):
##    print()
##
##    for row in range(9):
##        print(' '.join(str(item) for item in square_in[row]))
##
##    print()
##
###if row/col are omitted from call, 0 will be assumed for each
##def solve(puzzle, row=0, col=0):
##    
##    if col == 9:
##        row += 1
##        col = 0
##
##    if row == 9:
##        return puzzle
##    
##    if puzzle[row][col] != 0:
##        return solve(copy.deepcopy(puzzle), row, col+1)
##
##    else:
##        # get used values in row by making copy of current row and used in col with list[puzzle[i][col]]...
##        used = puzzle[row].copy() + list(puzzle[i][col] for i in range(9))
##
##        #get used values in square
##        start_row = 3 * (row // 3)
##        start_col = 3 * (col // 3)
##
##        for i in range(start_row, start_row+3):
##            for j in range(start_col, start_col+3):
##                used += [puzzle[i][j]]
##
##        #guess value
##        for guess in range(1,10):
##
##            if guess not in used:
##
##                puzzle[row][col] = guess
##
##                result = solve(copy.deepcopy(puzzle), row, col+1)
##
##                if result != False:
##                    return result
##
##        return False
##
##solved = solve(square)
##
##if solved == False:
##    print('\nNot Solvable')
##else:
##    print('\nSolved:')
##    display(solved)
