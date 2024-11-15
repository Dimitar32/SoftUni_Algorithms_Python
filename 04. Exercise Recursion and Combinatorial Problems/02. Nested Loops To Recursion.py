def generate_all_combinations(num, idx, vector):
    if idx >= len(vector):
        print (*vector, sep = ' ')
        return
    for i in range(1, num + 1):
        vector[idx] = i
        generate_all_combinations(num, idx + 1, vector)

n = int(input())
vector = [0] * n

generate_all_combinations(n, 0, vector)