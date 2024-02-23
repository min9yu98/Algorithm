import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
visited = [[False] * (m) for _ in range(n)]


def dfs(x, y):
    global cnt
    visited[y][x] = True
    if graph[y][x] == 'P':
        cnt += 1
    for i in range(4):
        dx, dy = x + move[i][0], y + move[i][1]
        if 0 <= dx < m and 0 <= dy < n:
            if not visited[dy][dx] and graph[dy][dx] != 'X':
                dfs(dx, dy)


cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            dfs(j, i)
print('TT' if not cnt else cnt)
