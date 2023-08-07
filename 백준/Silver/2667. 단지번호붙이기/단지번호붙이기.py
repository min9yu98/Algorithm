import sys

sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(x, y, cnt):
    graph[y][x] = 0
    for dx, dy in d:
        X, Y = dx + x, dy + y
        if (0 <= X < N) and (0 <= Y < N) and graph[Y][X]:
            cnt = dfs(X, Y, cnt + 1)
    return cnt


cnt = []
for y in range(N):
    for x in range(N):
        if graph[y][x]:
            cnt.append(dfs(x, y, cnt=1))

print(len(cnt))
cnt.sort()
for e in cnt:
    print(e)
