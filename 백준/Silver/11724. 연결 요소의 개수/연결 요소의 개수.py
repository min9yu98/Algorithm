import sys
from collections import deque
sys.setrecursionlimit(10000)

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)


def dfs(num):
    visited[num] = True
    for k in graph[num]:
        if not visited[k]:
            dfs(k)


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        result += 1
print(result)