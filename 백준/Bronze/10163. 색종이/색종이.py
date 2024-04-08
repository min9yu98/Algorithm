import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
graph = [[0] * 1002 for _ in range(1002)]
for i in range(1, n + 1):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y1 + y2):
        for k in range(x1, x1 + x2):
            graph[j][k] = i
for i in range(1, n + 1):
    cnt = 0
    for j in range(1002):
        cnt += graph[j].count(i)
    print(cnt)
