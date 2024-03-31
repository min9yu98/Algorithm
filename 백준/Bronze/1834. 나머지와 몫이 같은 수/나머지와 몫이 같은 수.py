import sys

input = sys.stdin.readline

n = int(input())
cnt = 0
for i in range(1, n):
    cnt += (n * i) + i
print(cnt)
