import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

move_x = [0, 0, 1, -1]
move_y = [1, -1, 0, 0]


def dfs(x, y, cnt, total):
    global res
    if res >= total + max_pos * (4 - cnt):
        return
    if cnt == 4:
        res = max(res, total)
        return
    for i in range(4):
        dx, dy = x + move_x[i], y + move_y[i]
        if 0 <= dx < m and 0 <= dy < n and not visited[dy][dx]:
            if cnt == 2:
                visited[dy][dx] = 1
                dfs(x, y, cnt + 1, total + board[dy][dx])
                visited[dy][dx] = 0
            visited[dy][dx] = 1
            dfs(dx, dy, cnt + 1, total + board[dy][dx])
            visited[dy][dx] = 0


max_pos = max(map(max, board))
res = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(j, i, 1, board[i][j])
        visited[i][j] = 0
print(res)
