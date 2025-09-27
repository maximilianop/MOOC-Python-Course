# Write your solution here
def row_correct(sudoku: list, row_no: int):
    row = []
    for val in sudoku[row_no]:
        if val != 0 and row.count(val) > 0:
            return False
        else:
            row.append(val)
    return True