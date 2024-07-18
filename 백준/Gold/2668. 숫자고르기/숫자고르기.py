import sys

input = sys.stdin.readline

n = int(input())
ans = []
visited = [0] * (n + 1)
grid = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    x = int(input())
    grid[x].append(i)


def dfs(v, i):
    visited[v] = 1
    for e in grid[v]:
        if not visited[e]:
            dfs(e, i)
        elif visited[e] and e == i:
            ans.append(e)


for i in range(1, n + 1):
    visited = [0] * (n + 1)
    dfs(i, i)
print(len(ans))
for i in ans:
    print(i)
