import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline
move_x = [1, -1, 1, -1, 0, 0, 1, -1]
move_y = [1, -1, -1, 1, 1, -1, 0, 0]


def bfs(x, y):
    queue = deque([(x, y)])
    graph[y][x] = 0
    while queue:
        lx, ly = queue.popleft()
        for i in range(8):
            dx = lx + move_x[i]
            dy = ly + move_y[i]
            if 0 <= dx < w and 0 <= dy < h and graph[dy][dx] == 1:
                graph[dy][dx] = 0
                queue.append((dx, dy))
    return 1


while True:
    w, h = map(int, input().split())
    graph = []
    if w == 0 and h == 0:
        break
    for _ in range(h):
        row = list(map(int, input().split()))
        graph.append(row)

    result = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                result += bfs(j, i)
    print(result)
