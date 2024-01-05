import sys
from collections import deque
sys.setrecursionlimit(10000)

_input = sys.stdin.readline

move_x = [1, -1, 0, 0]
move_y = [0, 0, 1, -1]


def dfs(x, y):
    for i in range(4):
        dx = x + move_x[i]
        dy = y + move_y[i]
        if 0 <= dx < m and 0 <= dy < n:
            if graph[dy][dx]:
                graph[dy][dx] = False
                dfs(dx, dy)


for _ in range(int(_input())):
    result = 0
    m, n, k = map(int, _input().split())
    graph = [[False] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, _input().split())
        graph[b][a] = True

    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                dfs(j, i)
                result += 1

    print(result)
