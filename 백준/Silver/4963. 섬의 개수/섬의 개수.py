import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline
move_x = [1, -1, 1, -1, 0, 0, 1, -1]
move_y = [1, -1, -1, 1, 1, -1, 0, 0]


def dfs(x, y):
    graph[y][x] = 0
    for i in range(8):
        dx = x + move_x[i]
        dy = y + move_y[i]
        if 0 <= dx < w and 0 <= dy < h:
            if graph[dy][dx] == 1:
                dfs(dx, dy)


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
                dfs(j, i)
                result += 1
    print(result)
