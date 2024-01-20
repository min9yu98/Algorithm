import sys
from collections import deque

input = sys.stdin.readline

gears = [deque(list(map(int,input().rstrip()))) for _ in range(4)]
k = int(input())
cnt = 0
for _ in range(k):
    init_r = []
    for i in range(4):
        init_r.append([gears[i][6], gears[i][2]])
    g, d = map(int, input().split())
    g -= 1
    if g != 0:
        for i in range(g, 0, -1):
            if init_r[i][0] != init_r[i - 1][1]:
                if (g - (i - 1)) % 2 == 0:
                    gears[i - 1].rotate(d)
                else:
                    gears[i - 1].rotate(0 - d)
            else:
                break
    if g != 3:
        for i in range(g, 3):
            if init_r[i][1] != init_r[i + 1][0]:
                if (g - (i + 1)) % 2 == 0:
                    gears[i + 1].rotate(d)
                else:
                    gears[i + 1].rotate(0 - d)
            else:
                break
    gears[g].rotate(d)


if gears[0][0] == 1:
    cnt += 1
if gears[1][0] == 1:
    cnt += 2
if gears[2][0] == 1:
    cnt += 4
if gears[3][0] == 1:
    cnt += 8

print(cnt)
