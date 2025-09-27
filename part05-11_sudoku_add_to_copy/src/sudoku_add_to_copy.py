# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    newSudoku = []
    for row in sudoku:
        newSudoku.append(row[:])
    newSudoku[row_no][column_no] = number
    return newSudoku