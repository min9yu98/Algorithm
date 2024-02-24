import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

for _ in range(int(input())):
    h, w = map(int, input().split())
    graph = [list(input().strip()) for _ in range(h)]
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(x, y):
        graph[y][x] = '@'
        for mx, my in move:
            dx, dy = x + mx, y + my
            if 0 <= dx < w and 0 <= dy < h:
                if graph[dy][dx] == '#':
                    dfs(dx, dy)


    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '#':
                dfs(j, i)
                cnt += 1
    print(cnt)
