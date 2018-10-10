'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''


def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    #print(sudoku)
    c = 0
    for row in sudoku:
        if len(set(row)) == 9 and int(max(row))-int(min(row)) == 8:
            c += 1
    for out in range(0, 9):
        mat1 = []
        for inside in range(0, 9):
            mat1.append(sudoku[inside][out])
        if len(set(mat1)) == 9 and int(max(mat1))-int(min(mat1)) == 8:
            c += 1
    for _ in range(0, 9):
        mat1 = []
        mat2 = []
        mat3 = []
        for out in range(0, 3):
            for inside in range(0, 3):
                mat1.append(sudoku[out][inside])
            for inside in range(3, 4):
                mat2.append(sudoku[out][inside])
            for inside in range(4, 9):
                mat3.append(sudoku[out][inside])
        for out in range(3, 4):
            for inside in range(0, 3):
                mat1.append(sudoku[out][inside])
            for inside in range(3, 4):
                mat2.append(sudoku[out][inside])
            for inside in range(4, 9):
                mat3.append(sudoku[out][inside])
        for out in range(4, 9):
            for inside in range(0, 3):
                mat1.append(sudoku[out][inside])
            for inside in range(3, 4):
                mat2.append(sudoku[out][inside])
            for inside in range(4, 9):
                mat3.append(sudoku[out][inside])
        if len(set(mat1)) == 9 and int(max(mat1))-int(min(mat1)) == 8:
            c += 1
        if len(set(mat2)) == 9 and int(max(mat2))-int(min(mat2)) == 8:
            c += 1
        if len(set(mat3)) == 9 and int(max(mat3))-int(min(mat3)) == 8:
            c += 1
    if c == 45:
        return True
    return False
def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    # initialize empty list
    sudoku = []
   # loop to read 9 lines of input from console
    for _ in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()
