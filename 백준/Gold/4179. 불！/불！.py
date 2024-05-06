import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
graph = []

q_j = deque()
q_f = deque()

visited_j = [[0] * c for _ in range(r)]
visited_f = [[0] * c for _ in range(r)]

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(r):
    s = input().strip()
    for j in range(c):
        if s[j] == 'F':
            q_f.append([j, i])
            visited_f[i][j] = 1
        elif s[j] == 'J':
            q_j.append([j, i])
            visited_j[i][j] = 1

    graph.append(s)

def bfs():
    while q_f:
        fx, fy = q_f.popleft()
        for mx, my in move:
            lx, ly = mx + fx, my + fy
            if 0 <= lx < c and 0 <= ly < r:
                if not visited_f[ly][lx] and graph[ly][lx] != '#':
                    visited_f[ly][lx] = visited_f[fy][fx] + 1
                    q_f.append([lx, ly])
    while q_j:
        jx, jy = q_j.popleft()
        for mx, my in move:
            lx, ly = jx + mx, jy + my
            if 0 <= lx < c and 0 <= ly < r:
                if not visited_j[ly][lx] and graph[ly][lx] != '#':
                    if not visited_f[ly][lx] or visited_j[jy][jx] + 1 < visited_f[ly][lx]:
                        visited_j[ly][lx] = visited_j[jy][jx] + 1
                        q_j.append([lx, ly])
            else:
                return visited_j[jy][jx]
    return "IMPOSSIBLE"


print(bfs())
