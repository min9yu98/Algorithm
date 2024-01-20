import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]


def dfs(n, i):
    global result
    total = 0
    if n == M:
        for h in home_loc:
            hc, hr = h[0], h[1]
            dist = 2 * N
            for c in select:
                cc, cr = c[0], c[1]
                tmp = abs(cc - hc) + abs(cr - hr)
                if tmp < dist:
                    dist = tmp
            total += dist
        if total < result:
            result = total
            return
    for idx in range(i, k):
        select.append(chicken_loc[idx])
        dfs(n + 1, idx + 1)
        select.pop()


chicken_loc = deque([])
home_loc = deque([])
select = deque([])
for i in range(N):
    for j in range(N):
        if road[i][j] == 2:
            chicken_loc.append([j, i])
        elif road[i][j] == 1:
            home_loc.append([j, i])
k = len(chicken_loc)
result = N * 2 * len(home_loc)
for i in range(k):
    dfs(0, i)
print(result)
