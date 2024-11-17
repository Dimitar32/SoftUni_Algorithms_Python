def find_new_area(matrix):
    for i in range(0, len(matrix[0])):
        if matrix[0][i] == '-':
            return i
    return -1

def con_areas():
    return