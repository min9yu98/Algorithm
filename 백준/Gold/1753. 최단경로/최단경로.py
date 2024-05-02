import heapq
import sys

input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
distances = [float('inf')] * (v + 1)
queue = []
graph = [[] for _ in range(v + 1)]


def dijkstra(start):
    distances[start] = 0
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)
        if distances[current_destination] < current_distance:
            continue
        for new_destination, new_distance in graph[current_destination]:
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
    return distances


for _ in range(e):
    x, y, w = map(int, input().split())
    graph[x].append([y, w])

for ans in dijkstra(k)[1:]:
    if ans == float('inf'):
        print('INF')
    else:
        print(ans)
