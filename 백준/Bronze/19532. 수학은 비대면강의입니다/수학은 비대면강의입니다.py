import sys

input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

flag = False
for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (i * a) + (j * b) == c and (d * i) + (e * j) == f:
            print(i, j)
            flag = True
            break
    if flag:
        break