import sys
from collections import deque

input = sys.stdin.readline

graph = [list(input().strip()) for _ in range(12)]
visited = [[0] * 6 for _ in range(12)]
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(x, y):
    queue = deque([(x, y)])
    same = []
    while queue:
        x, y = queue.popleft()
        same.append((x, y))
        visited[y][x] = True
        for ex, ey in move:
            mx, my = x + ex, y + ey
            if 0 <= mx < 6 and 0 <= my < 12 and graph[y][x] == graph[my][mx] and not visited[my][mx]:
                queue.append((mx, my))
    return same


def delete(same):
    for x, y in same:
        graph[y][x] = '.'


def down():
    for x in range(6):
        for y in range(10, -1, -1):
            for k in range(11, y, -1):
                if graph[y][x] != '.' and graph[k][x] == '.':
                    graph[k][x] = graph[y][x]
                    graph[y][x] = '.'


ans = 0
while True:
    bust = False
    visited = [[False] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and not visited[i][j]:
                same_block = bfs(j, i)
                if len(same_block) >= 4:
                    bust = True
                    delete(same_block)
    if bust:
        down()
        ans += 1
    else:
        break
print(ans)
