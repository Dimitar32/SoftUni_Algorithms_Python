def dfs(node, graph, visited):
    if node in visited:
        return

    visited.add(node)

    for child in graph[node]:
        dfs(child, graph, visited)

    print(node, end=' ')


graph = {
    0: [],
    1: [0, 1]
}

visited = set()

for node in graph:
    dfs(node, graph, visited)