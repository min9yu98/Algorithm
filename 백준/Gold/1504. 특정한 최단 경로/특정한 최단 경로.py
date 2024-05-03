import sys
import heapq

input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

def dijkstra(start):
    distances = [float('inf') for _ in range(n + 1)]
    queue = []

    distances[start] = 0
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if distances[current_node] < current_distance:
            continue
        for new_node, new_distance in graph[current_node]:
            distance = new_distance + current_distance
            if distance < distances[new_node]:
                distances[new_node] = distance
                heapq.heappush(queue, [distance, new_node])
    return distances


for _ in range(e):
    x, y, w = map(int, input().split())
    graph[x].append([y, w])
    graph[y].append([x, w])

v1, v2 = map(int, input().split())

start_to_v1 = dijkstra(1)[v1]
start_to_v2 = dijkstra(1)[v2]

v1_path = start_to_v1 + dijkstra(v1)[v2] + dijkstra(v2)[n]
v2_path = start_to_v2 + dijkstra(v2)[v1] + dijkstra(v1)[n]

print(min(v1_path, v2_path) if min(v1_path, v2_path) != float('inf') else -1)
