import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    x, y, w = map(int, input().split())
    graph[x][y] = min(w, graph[x][y])

for i in range(1, n + 1):
    graph[i][i] = 0

for middle in range(1, n + 1):  # middle
    for start in range(1, n + 1):  # start
        for end in range(1, n + 1):  # end
            graph[start][end] = min(graph[start][end], graph[start][middle] + graph[middle][end])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
