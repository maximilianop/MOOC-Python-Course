# Write your solution here
def print_sudoku(sudoku: list):
    for i in range(0, len(sudoku)):
        for j in range(0, len(sudoku)):
            if sudoku[i][j] == 0:
                print('_ ', end='')
            else:
                print(f'{sudoku[i][j]} ', end='')
            if j == 2 or j == 5:
                print(' ',  end='')
        print()
        if i == 2 or i == 5:
            print()

def add_number(sudoku: list, row_no: int, column_no: int, number: int): 
    sudoku[row_no][column_no] = number

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print_sudoku(sudoku)
