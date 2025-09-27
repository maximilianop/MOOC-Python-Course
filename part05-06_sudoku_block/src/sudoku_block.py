# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    dupes = []
    for row in range(row_no, row_no + 3):
        for col in range(column_no, column_no + 3):
            val = sudoku[row][col]
            if val > 0 and val in dupes:
                return False
            dupes.append(val)
    return True