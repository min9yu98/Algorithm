import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
maxi = 0


def bfs(x, y):
    global maxi
    queue = deque([])
    queue.append((x, y))
    graph[y][x] = 0
    cnt = 0
    while queue:
        lx, ly = queue.popleft()
        cnt += 1
        for mx, my in move:
            dx, dy = lx + mx, ly + my
            if 0 <= dx < m and 0 <= dy < n:
                if graph[dy][dx]:
                    graph[dy][dx] = 0
                    queue.append((dx, dy))
    maxi = max(maxi, cnt)


total = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            bfs(j, i)
            total += 1
print(total)
print(maxi)
