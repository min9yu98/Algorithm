import sys
input = sys.stdin.readline

n = int(input())
x_min, x_max = 10001, -10001
y_min, y_max = 10001, -10001

for _ in range(n):
    a, b = map(int, input().split())
    x_min, x_max = min(x_min, a), max(x_max, a)
    y_min, y_max = min(y_min, b), max(y_max, b)

if n == 1:
    print(0)
    exit(0)
print((x_max - x_min) * (y_max - y_min))
