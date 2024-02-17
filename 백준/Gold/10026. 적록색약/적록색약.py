from copy import deepcopy
from collections import deque

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

n = int(input())
board = [list(input()) for _ in range(n)]
board_dup = deepcopy(board)
for i in range(n):
    for j in range(n):
        if board_dup[i][j] == 'G':
            board_dup[i][j] = 'R'
visited = [[False] * n for _ in range(n)]
visited_dup = deepcopy(visited)

ans1 = 0
ans2 = 0


def bfs(x, y, color):
    queue = deque([(x, y)])
    while queue:
        lx, ly = queue.popleft()
        for i in range(4):
            dx, dy = move[i][0] + lx, move[i][1] + ly
            if 0 <= dx < n and 0 <= dy < n and not visited[dy][dx] and color == board[dy][dx]:
                queue.append((dx, dy))
                visited[dy][dx] = True


def bfs_dup(x, y, color):
    queue = deque([(x, y)])
    while queue:
        lx, ly = queue.popleft()
        for i in range(4):
            dx, dy = move[i][0] + lx, move[i][1] + ly
            if 0 <= dx < n and 0 <= dy < n and not visited_dup[dy][dx] and color == board_dup[dy][dx]:
                queue.append((dx, dy))
                visited_dup[dy][dx] = True


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(j, i, board[i][j])
            ans1 += 1
        if not visited_dup[i][j]:
            bfs_dup(j, i, board_dup[i][j])
            ans2 += 1
print(ans1, ans2)
