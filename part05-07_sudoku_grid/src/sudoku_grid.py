# Write your solution here
def row_correct(sudoku: list, row_no: int):
    row = []
    for val in sudoku[row_no]:
        if val != 0 and row.count(val) > 0:
            return False
        else:
            row.append(val)
    return True

def column_correct(sudoku: list, column_no: int):
    dupes = []
    for row in sudoku:
        if row[column_no] > 0 and row[column_no] in dupes:
            return False
        dupes.append(row[column_no])
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    dupes = []
    for row in range(row_no, row_no + 3):
        for col in range(column_no, column_no + 3):
            val = sudoku[row][col]
            if val > 0 and val in dupes:
                return False
            dupes.append(val)
    return True

def sudoku_grid_correct(sudoku: list):
    for row in range(0, len(sudoku)):
        if not row_correct(sudoku, row):
            return False
    for col in range(0, len(sudoku[0])):
        if not column_correct(sudoku, col):
            return False
    for row in range(0, 7, 3):
        for col in range(0, 7, 3):
            if not block_correct(sudoku, row, col):
                return False
    return True