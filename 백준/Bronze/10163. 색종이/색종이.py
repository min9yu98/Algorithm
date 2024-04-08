import sys

input = sys.stdin.readline

n = int(input())
graph = [[0] * 102 for _ in range(102)]
for i in range(1, n + 1):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y1 + y2):
        for k in range(x1, x1 + x2):
            graph[j][k] = i
for i in range(1, n + 1):
    cnt = 0
    for j in range(102):
        cnt += graph[j].count(i)
    print(cnt)
