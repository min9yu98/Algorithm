import sys

sys.setrecursionlimit(100000)


def dfs(x, y, k):
    visited[y][x] = True
    for dx, dy in mov:
        Dx, Dy = x + dx, y + dy
        if 0 <= Dx < n and 0 <= Dy < n and graph[Dy][Dx] > k and not visited[Dy][Dx]:
            dfs(Dx, Dy, k)


n = int(input())
graph = []
mov = [(1, 0), (-1, 0), (0, 1), (0, -1)]
maxi = 0
for _ in range(n):
    m = list(map(int, input().rstrip().split()))
    if maxi < max(m):
        maxi = max(m)
    graph.append(list(m))

ans = 1
for k in range(maxi):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and not visited[i][j]:
                cnt += 1
                visited[i][j] = True
                dfs(j, i, k)
    ans = max(ans, cnt)
print(ans)
