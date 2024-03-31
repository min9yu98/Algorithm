import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [input().strip() for _ in range(n)]
pos = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'X':
            pos.append((j, i))

pos.sort(key=lambda x: (x[0], x[1]))
x_pos = [0] * m
y_pos = [0] * n
for p in pos:
    x_pos[p[0]] = 1
    y_pos[p[1]] = 1
print(max(x_pos.count(0), y_pos.count(0)))

