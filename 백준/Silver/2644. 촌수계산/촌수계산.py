import sys
sys.setrecursionlimit(100000)

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = []

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(v, num):
    num += 1
    visited[v] = True

    if v == b:
        result.append(num)

    for e in graph[v]:
        if not visited[e]:
            dfs(e, num)

dfs(a, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)
