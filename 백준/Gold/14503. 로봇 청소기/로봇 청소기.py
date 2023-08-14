import sys

sys.setrecursionlimit(100000)



N, M = map(int, input().split())
y, x, d = map(int, input().split())
visited = [[False] * M for _ in range(N)]
graph = [list(map(int, input().split())) for _ in range(N)]
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]


visited[y][x] = True
cnt = 1
while True:
    flag = 0
    for _ in range(4):
        d = (d + 3) % 4
        nx = x + move[d][1]
        ny = y + move[d][0]

        if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 0:
            if not visited[ny][nx]:
                visited[ny][nx] = True
                cnt += 1
                x, y = nx, ny
                flag = 1
                break
    if flag == 0:
        if graph[y - move[d][0]][x - move[d][1]] == 1:
            print(cnt)
            break
        else:
            x, y = x - move[d][1], y - move[d][0]