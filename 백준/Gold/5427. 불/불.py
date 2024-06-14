import sys
from collections import deque

input = sys.stdin.readline

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(f_s, queue, visit):
    while queue:
        x, y, time = queue.popleft()
        for mx, my in move:
            nx, ny = x + mx, y + my
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == '.' or graph[nx][ny] == '@':
                    if visit[nx][ny] > time + 1:
                        visit[nx][ny] = time + 1
                        queue.append((nx, ny, visit[nx][ny]))
            elif f_s == 's':
                print(time + 1)
                return
    if f_s == 's':
        print('IMPOSSIBLE')


for _ in range(int(input())):
    w, h = map(int, input().split())
    graph = [[0] * w for _ in range(h)]
    visit = [[1e9] * w for _ in range(h)]

    fqueue = deque()
    squeue = deque()
    for i in range(h):
        tmp = input().strip()
        for j in range(w):
            graph[i][j] = tmp[j]
            if tmp[j] == '@':
                squeue.append((i, j, 0))
            elif tmp[j] == '*':
                visit[i][j] = 0
                fqueue.append((i, j, 0))
    bfs('f', fqueue, visit)
    bfs('s', squeue, visit)