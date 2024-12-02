def bubble_sort(array):
    for i in range (len(array)):
        for j in range(1, len(array) - i):
            if array[j - 1] > array[j]:
                array[j], array[j - 1] = array[j - 1], array[j]

    return array


array = list(map(int, input().split()))
bubble_sort(array)

print(' '.join(map(str, array)))