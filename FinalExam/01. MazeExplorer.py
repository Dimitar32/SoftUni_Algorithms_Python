from collections import deque

def shortest_path_in_maze(n, maze):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def find_positions():
        start = end = None
        for i in range(n):
            for j in range(n):
                if maze[i][j] == 'S':
                    start = (i, j)
                elif maze[i][j] == 'E':
                    end = (i, j)
        return start, end

    def bfs(start, end):
        queue = deque([(start[0], start[1], 0)])
        visited = [[False] * n for _ in range(n)]
        visited[start[0]][start[1]] = True

        while queue:
            x, y, steps = queue.popleft()

            if (x, y) == end:
                return steps

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and maze[nx][ny] != '#':
                    visited[nx][ny] = True
                    queue.append((nx, ny, steps + 1))

        return -1

    start, end = find_positions()
    return bfs(start, end)


n = int(input())
maze = [input().strip() for _ in range(n)]
print(shortest_path_in_maze(n, maze))  
