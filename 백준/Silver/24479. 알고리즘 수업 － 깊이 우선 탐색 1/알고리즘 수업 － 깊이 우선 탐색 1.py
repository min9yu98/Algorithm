import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n + 1):
    if graph[i]:
        graph[i].sort()
order = 1


def dfs(k):
    global order
    visited[k] = order
    for e in graph[k]:
        if not visited[e]:
            order += 1
            dfs(e)


dfs(r)
for i in range(1, n + 1):
    print(visited[i])
