def find_best_sequence(goals):
    if not goals:
        return []

    best_sequence = []
    n = len(goals)

    for i in range(n):
        current_sequence = [goals[i]]
        for j in range(i + 1, n):
            if goals[j] >= current_sequence[-1]:
                current_sequence.append(goals[j])
        if len(current_sequence) > len(best_sequence):
            best_sequence = current_sequence

    return best_sequence

goals = input().split(', ')
best_sequence = find_best_sequence(goals)
print(" ".join(best_sequence))
