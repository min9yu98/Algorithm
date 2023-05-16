import sys
from collections import deque

sys.setrecursionlimit(1000000)



dx = [0, 1]
dy = [1, 0]

def dfs(x, y, v):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if v[x][y]:
        return False
    if graph[x][y] == -1:
        print("HaruHaru")
        exit()
    v[x][y] = True
    for i in range(2):
        nx = x + dx[i] * graph[x][y]
        ny = y + dy[i] * graph[x][y]
        dfs(nx, ny, v)
    return True


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
if dfs(0, 0, visited):
    print("Hing")
