import heapq

def find_shortest_path_with_closures():
    r = int(input())

    graph = {}
    for _ in range(r):
        city1, _, city2, _, distance = input().split()
        distance = int(distance)

        if city1 not in graph:
            graph[city1] = []
        if city2 not in graph:
            graph[city2] = []

        graph[city1].append((city2, distance))
        graph[city2].append((city1, distance))

    closed_roads = input().split(',')
    closed_set = set()
    for road in closed_roads:
        if road:
            city1, city2 = road.split('-')
            closed_set.add((city1, city2))
            closed_set.add((city2, city1))

    start_city = input().strip()
    end_city = input().strip()

    def dijkstra(start, end):
        heap = [(0, start, [])]
        visited = set()

        while heap:
            cost, city, path = heapq.heappop(heap)

            if city in visited:
                continue
            visited.add(city)
            path = path + [city]

            if city == end:
                return cost, path

            for neighbor, distance in graph.get(city, []):
                if (city, neighbor) not in closed_set and neighbor not in visited:
                    heapq.heappush(heap, (cost + distance, neighbor, path))

        return float('inf'), []

    total_distance, path = dijkstra(start_city, end_city)

    if total_distance != float('inf'):
        print(" - ".join(path))
        print(total_distance)
    else:
        print("No path found")


find_shortest_path_with_closures()
