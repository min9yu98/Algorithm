import sys
from copy import deepcopy

input = sys.stdin.readline

n = int(input())
loc = [list(map(int, input().split())) for _ in range(n)]
loc.sort()
start, end = loc[0][0], loc[0][1]
length = 0
for i in range(1, n):
    if end >= loc[i][1]:
        continue
    elif loc[i][0] <= end < loc[i][1]:
        end = loc[i][1]
    else:
        length += end - start
        start = loc[i][0]
        end = loc[i][1]
length += end - start
print(length)
