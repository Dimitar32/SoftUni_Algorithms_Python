def reverse_array(array, index, new_array):
    if index < 0:
        return
    if index + 1 == len(array):
        new_array.append(array[index])
        del array[index]
        reverse_array(array, index - 1, new_array)



numbers = [int(x) for x in input().split()]
result = []
reverse_array(numbers, len(numbers) - 1, result)

print(" ".join(map(str, result)))