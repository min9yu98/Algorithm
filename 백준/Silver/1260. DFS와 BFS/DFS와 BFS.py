import sys
from collections import deque


n, m, v = map(int, input().split())
visited_dfs = [False for _ in range(n + 1)]
visited_bfs = [False for _ in range(n + 1)]
graph = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True


def bfs(element):
    q = deque([element])
    visited_bfs[element] = True
    while q:
        element = q.popleft()
        print(element, end=" ")
        for i in range(1, n + 1):
            if not visited_bfs[i] and graph[element][i]:
                q.append(i)
                visited_bfs[i] = True


def dfs(element):
    visited_dfs[element] = True
    print(element, end=" ")
    for i in range(1, n + 1):
        if not visited_dfs[i] and graph[element][i]:
            dfs(i)


dfs(v)
print()
bfs(v)
