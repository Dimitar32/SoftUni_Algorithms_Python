def bin_search(array, num):
    for i, value in enumerate(array):
        if value == num:
            return i

    return -1

array = list(map(int, input().split()))

num = int(input())

index = bin_search(array, num)

print(index)