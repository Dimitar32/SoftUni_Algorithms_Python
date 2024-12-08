class Edge:
    def __init__(self, parent, child):
        self.parent = parent
        self.child = child


word = input()
graph = []

while word != 'End':
    nodes = word.split("-", 2)
    graph.append(Edge(nodes[0], nodes[1]))
    word = input()

adj_list = {}
for edge in graph:
    if edge.parent not in adj_list:
        adj_list[edge.parent] = []
    adj_list[edge.parent].append(edge.child)


def is_acyclic(graph):
    visited = set()
    stack = set()

    def dfs(node):
        if node in stack:
            return False
        if node in visited:
            return True

        stack.add(node)

        for neighbor in graph.get(node, []):
            if not dfs(neighbor):
                return False

        stack.remove(node)
        visited.add(node)
        return True

    for node in adj_list:
        if node not in visited:
            if not dfs(node):
                return False

    return True


if is_acyclic(adj_list):
    print("Acyclic: Yes")
else:
    print("Acyclic: No")