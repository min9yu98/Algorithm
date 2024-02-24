import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, list(input().strip()))) for _ in range(m)]
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(x, y):
    graph[y][x] = 2
    for i in range(4):
        dx, dy = x + move[i][0], y + move[i][1]
        if 0 <= dx < n and 0 <= dy < m:
            if graph[dy][dx] == 0:
                dfs(dx, dy)


for i in range(n):
    if graph[0][i] == 0:
        dfs(i, 0)
print("YES" if 2 in graph[-1] else "NO")
