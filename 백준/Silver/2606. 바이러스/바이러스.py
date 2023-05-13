import sys
from collections import deque

sys.setrecursionlimit(1000000)


n = int(input())
m = int(input())
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
cnt = 0


for _ in range(m):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]


def dfs(x):
    global cnt
    visited[x] = True
    cnt += 1
    for i in graph[x]:
        if not visited[i]:
            dfs(i)


dfs(1)
print(cnt - 1)
