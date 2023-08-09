import sys
from collections import deque


def bfs():
    q = deque()
    q.append([home[0], home[1]])
    while q:
        v = q.popleft()
        x, y = v[0], v[1]
        if abs(x - fest[0]) + abs(y - fest[1]) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                dx, dy = conv[i][0], conv[i][1]
                if abs(dx - x) + abs(dy - y) <= 1000:
                    q.append([dx, dy])
                    visited[i] = True
    print("sad")
    return


for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    home = list(map(int, sys.stdin.readline().split()))
    conv = []
    for _ in range(n):
        c = list(map(int, sys.stdin.readline().split()))
        conv.append(c)
    fest = list(map(int, input().split()))
    visited = [False] * (n + 1)
    bfs()