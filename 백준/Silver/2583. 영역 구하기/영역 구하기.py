import sys
from collections import deque

input = sys.stdin.readline

m, n, k = map(int, input().split())
visited = [[0] * n for _ in range(m)]
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            if not visited[y][x]:
                visited[y][x] = 1


def bfs(x, y):
    cnt = 1
    queue = deque([(x, y)])
    visited[y][x] = 1
    while queue:
        lx, ly = queue.popleft()
        for mx, my in move:
            dx, dy = lx + mx, ly + my
            if 0 <= dx < n and 0 <= dy < m:
                if not visited[dy][dx]:
                    visited[dy][dx] = 1
                    queue.append((dx, dy))
                    cnt += visited[dy][dx]
    return cnt


total_cnt = 0
result = []
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            result.append(bfs(j, i))
            total_cnt += 1
print(total_cnt)
result.sort()
print(' '.join(list(map(str, result))))
