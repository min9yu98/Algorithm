import sys
from collections import deque

sys.setrecursionlimit(1000000)



def dfs(x, y):
    visited[x][y] = True
    if graph[x][y] == '-':
        if y + 1 < m and graph[x][y + 1] == '-' and not visited[x][y + 1]:
            dfs(x, y + 1)
    elif graph[x][y] == '|':
        if x + 1 < n and graph[x + 1][y] == '|' and not visited[x + 1][y]:
            dfs(x + 1, y)
    return


n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j)
            cnt += 1
print(cnt)
