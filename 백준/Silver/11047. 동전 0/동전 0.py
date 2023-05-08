import sys


n, k = map(int, input().split())
lst = sorted([int(input()) for _ in range(n)], reverse=True)
cnt = 0

for i in range(n):
    if lst[i] > k:
        continue
    cnt += k // lst[i]
    k %= lst[i]

print(cnt)