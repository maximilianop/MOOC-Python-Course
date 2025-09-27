# Write your solution here
def transpose(matrix: list):
    for i in range(0, len(matrix[0])):
        for j in range(i, len(matrix[i])):
            temp = matrix[j][i]
            matrix[j][i] = matrix[i][j]
            matrix[i][j] = temp
 