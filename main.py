
GRID_SIZE = 9

sudoku_grid = [
    [4, 0, 0, 0, 5, 0, 8, 0, 0],
    [0, 1, 8, 0, 0, 0, 7, 0, 0],
    [0, 0, 3, 0, 0, 4, 0, 0, 0],
    [9, 6, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 5, 0, 0, 3, 0, 0, 0],
    [0, 7, 0, 0, 0, 8, 0, 6, 0],
    [0, 0, 1, 6, 0, 0, 0, 0, 4],
    [0, 0, 0, 5, 0, 0, 0, 1, 3],
    [0, 0, 0, 8, 0, 0, 0, 0, 0]
    ]


def print_sudoku():
    """
    Simply print out the sudoku array.
    :return: Nothing.
    """
    for cell in sudoku_grid:
        print(cell)


def cell_is_empty():
    """
    Process grid cells that have not been solved.
    :return: A list containing the cell details.
    """
    for i in range(0, GRID_SIZE):
        for j in range(0, GRID_SIZE):
            # If we have an empty cell...
            if sudoku_grid[i][j] == 0:
                row = i
                col = j
                return row, col, True
    return -1, -1, False


def number_already_exists(number, row, column):
    """
    Checks if a number already exists in a row, column or sub-grid.
    :param number: The number to check for.
    :param row: The row to check.
    :param column: The column to check.
    :return: True if the number is ok, False if the number already exists.
    """

    # Process the row, return false if the same number already exists.
    for i in range(0, GRID_SIZE):
        if sudoku_grid[row][i] == number:
            return False

    # Process the column, return false if the same number already exists.
    for i in range(0, GRID_SIZE):
        if sudoku_grid[i][column] == number:
            return False
    row_start = (row // 3) * 3
    col_start = (column // 3) * 3

    # Process the sub-grid, return false if the same number already exists.
    for i in range(row_start, row_start+3):
        for j in range(col_start, col_start+3):
            if sudoku_grid[i][j] == number:
                return False
    return True


def solve_sudoku():
    """
    The top level function for solving the sudoku puzzle.
    :return: True if solved, False otherwise.
    """
    # Check the current state of the sudoku grid.
    # Return false when an empty cell is found.
    row, col, cell_status = cell_is_empty()

    if not cell_status:
        return True

    for i in range(1, 10):
        # Check if we can assign the current number.
        if number_already_exists(i, row, col):
            sudoku_grid[row][col] = i

            # Move back and try again if the number doesn't fit.
            if solve_sudoku():
                return True

            # In this case, the number does not fit, try again.
            sudoku_grid[row][col] = 0
    return False


if solve_sudoku():
    print_sudoku()
else:
    print("No solution found")
