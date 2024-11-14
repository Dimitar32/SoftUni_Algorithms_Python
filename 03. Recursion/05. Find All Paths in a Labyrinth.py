def find_all_path(row, col, matrix, direction, path):
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
        return
    if lab[row][col] == 'e':
        path.append(direction)
        print(''.join(path))
        path.pop()
        return
    if lab[row][col] == '*':
        return
    if lab[row][col] == 'v':
        return

    lab[row][col] = 'v'
    path.append(direction)

    find_all_path(row - 1, col, matrix, 'U', path)
    find_all_path(row + 1, col, matrix, 'D', path)
    find_all_path(row, col - 1, matrix, 'L', path)
    find_all_path(row, col + 1, matrix, 'R', path)

    path.pop()
    lab[row][col] = '-'



rows = int(input())
cols = int(input())

lab = []

for _ in range(rows):
    lab.append(list(input()))

find_all_path(0, 0, lab, '', [])