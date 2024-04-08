import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]

matrix = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for l in range(m):
            matrix[i][j] += a[i][l] * b[l][j]
for e in matrix:
    for num in e:
        print(num, end=' ')
    print()


