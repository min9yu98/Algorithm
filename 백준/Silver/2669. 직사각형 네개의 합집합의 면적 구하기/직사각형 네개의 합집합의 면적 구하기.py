import sys
from copy import deepcopy

input = sys.stdin.readline

grid = [[0] * 101 for _ in range(101)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[j][i] = 1
cnt = 0
for e in grid:
    cnt += e.count(1)
print(cnt)
