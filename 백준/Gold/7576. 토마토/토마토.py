from collections import deque

move_x = [0, 0, -1, 1]
move_y = [1, -1, 0, 0]

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
queue = deque([])
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((j, i))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        dx, dy = x + move_x[i], y + move_y[i]
        if 0 <= dx < m and 0 <= dy < n:
            if graph[dy][dx] == 0:
                graph[dy][dx] = graph[y][x] + 1
                queue.append((dx, dy))
for i in range(n):
    if graph[i].count(0) != 0:
        print(-1)
        exit(0)
    cnt = max(cnt, max(graph[i]))
print(cnt - 1)
