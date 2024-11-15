def move_all_paths(rows, cols, row, col, matrix, sum):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return
    if matrix[row][col] == 'End':
        sum[0] += 1
        return
    if matrix[row][col] == 'v':
        return

    matrix[row][col] = 'v'

    move_all_paths(rows, cols, row - 1, col, matrix, sum)
    move_all_paths(rows, cols, row + 1, col, matrix, sum)
    move_all_paths(rows, cols, row, col - 1, matrix, sum)
    move_all_paths(rows, cols, row, col + 1, matrix, sum)

    matrix[row][col] = 0

sum = []
sum.append(0)
rows = int(input())
cols = int(input())
matrix = [[0] * cols for _ in range(rows)]
matrix[rows - 1][cols - 1] = 'End'

move_all_paths(rows, cols, 0, 0, matrix, sum)

print (sum[0])