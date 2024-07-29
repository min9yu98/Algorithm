import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
surround = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(x, y):
    queue = deque([])
    queue.append([x, y])
    visited[x][y] = 1
    melting = []
    while queue:
        current_x, current_y = queue.popleft()
        melting_value = 0
        for dx, dy in surround:
            lx, ly = dx + current_x, dy + current_y
            if 0 <= lx < n and 0 <= ly < m:
                if graph[lx][ly] == 0:
                    if graph[current_x][current_y] > 0:
                        melting_value += 1
                elif graph[lx][ly] != 0 and not visited[lx][ly]:
                    queue.append([lx, ly])
                    visited[lx][ly] = 1
        if graph[current_x][current_y]:
            melting.append([current_x, current_y, melting_value])
    for x, y, v in melting:
        if graph[x][y] < v:
            graph[x][y] = 0
        else:
            graph[x][y] -= v
    return 1


ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ice.append((i, j))

year = 0
while ice:
    visited = [[0] * m for _ in range(n)]
    delList = []
    group = 0
    for i, j in ice:
        if graph[i][j] and not visited[i][j]:
            group += bfs(i, j)
        if graph[i][j] == 0:
            delList.append((i, j))
    if group > 1:
        print(year)
        break
    ice = sorted(list(set(ice) - set(delList)))
    year += 1
if group < 2:
    print(0)

