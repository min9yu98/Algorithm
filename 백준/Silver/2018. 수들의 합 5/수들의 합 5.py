import sys
from copy import deepcopy

input = sys.stdin.readline

n = int(input())
x, y = 0, 0
cnt, total = 0, 0
while y <= n:
    if total < n:
        y += 1
        total += y
    elif total > n:
        total -= x
        x += 1
    else:
        cnt += 1
        y += 1
        total += y
print(cnt)
