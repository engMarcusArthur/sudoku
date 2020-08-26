grid_size = 9

sudoku_grid = [
    [0, 1, 0, 0, 8, 0, 0, 0, 0],
    [0, 9, 6, 2, 0, 7, 0, 0, 0],
    [0, 0, 8, 6, 0, 0, 5, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 0],
    [1, 0, 0, 7, 0, 5, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 1, 5, 7],
    [0, 0, 3, 0, 6, 1, 0, 0, 0],
    [0, 0, 0, 4, 0, 0, 7, 6, 3],
    [0, 0, 0, 0, 7, 0, 4, 0, 0]
    ]


def print_sudoku():
    """
    Simply print out the sudoku array.
    :return: Nothing.
    """
    for cell in sudoku_grid:
        print(cell)


#function to check if all cells are assigned or not
#if there is any unassigned cell
#then this function will change the values of
#row and col accordingly
def number_unassigned(row, col):
    """

    :param row:
    :param col:
    :return:
    """
    blank_cell = 0
    for i in range(0, grid_size):
        for j in range(0, grid_size):

            if sudoku_grid[i][j] == 0:
                row = i
                col = j
                blank_cell = 1
                a = [row, col, blank_cell]
                return a
    a = [-1, -1, blank_cell]
    return a

#function to check if we can put a
#value in a paticular cell or not
def is_safe(n, r, c):
    #checking in row
    for i in range(0, grid_size):
        #there is a cell with same value
        if sudoku_grid[r][i] == n:
            return False
    #checking in column
    for i in range(0, grid_size):
        #there is a cell with same value
        if sudoku_grid[i][c] == n:
            return False
    row_start = (r//3)*3
    col_start = (c//3)*3;
    #checking submatrix
    for i in range(row_start,row_start+3):
        for j in range(col_start,col_start+3):
            if sudoku_grid[i][j]==n:
                return False
    return True


def solve_sudoku():
    row = 0
    col = 0
    #if all cells are assigned then the sudoku is already solved
    #pass by reference because number_unassigned will change the values of row and col
    a = number_unassigned(row, col)
    if a[2] == 0:
        return True
    row = a[0]
    col = a[1]
    #number between 1 to 9
    for i in range(1, 10):
        #if we can assign i to the cell or not
        #the cell is matrix[row][col]
        if is_safe(i, row, col):
            sudoku_grid[row][col] = i
            #backtracking
            if solve_sudoku():
                return True
            #f we can't proceed with this solution
            #reassign the cell
            sudoku_grid[row][col] = 0
    return False

if solve_sudoku():
    print_sudoku()
else:
    print("No solution found")
