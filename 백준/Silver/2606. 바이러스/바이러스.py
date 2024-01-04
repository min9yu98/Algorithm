import sys
from collections import deque
_input = sys.stdin.readline

com = int(_input())
conn = int(_input())
visited = [False] * (com + 1)
graph = [[] * (com + 1) for _ in range(com + 1)]

for _ in range(conn):
    a, b = map(int, _input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0

queue = deque([1])
visited[1] = True
while queue:
    host = queue.popleft()
    for i in range(len(graph[host])):
        if not visited[graph[host][i]]:
            queue.append(graph[host][i])
            visited[graph[host][i]] = True
            result += 1

print(result)
