import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
road = [[] for _ in range(n + 1)]
distances = [float('inf')] * (n + 1)

for _ in range(m):
    x, y, w = map(int, input().split())
    road[x].append([y, w])
    road[y].append([x, w])


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distances[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist:
            continue
        for info in road[now]:
            if dist + info[1] < distances[info[0]]:
                distances[info[0]] = dist + info[1]
                heapq.heappush(q, (dist + info[1], info[0]))


dijkstra(1)
print(distances[n])
