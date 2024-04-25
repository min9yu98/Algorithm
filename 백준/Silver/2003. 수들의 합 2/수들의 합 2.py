from itertools import permutations
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

start, end = 0, 1
ans = 0
while end <= n and start <= end:
    total = sum(A[start:end])
    if total == m:
        ans += 1
        end += 1
    elif total > m:
        start += 1
    else:
        end += 1
print(ans)
