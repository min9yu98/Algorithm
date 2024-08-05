import sys
from copy import deepcopy

input = sys.stdin.readline

N = int(input())
t, p = [0] * (N + 1), [0] * (N + 1)
for i in range(1, N + 1):
    t[i], p[i] = map(int, input().split())
dp = [0] * (N + 1)

for i in range(1, N + 1):
    dp[i] = max(dp[i], dp[i - 1])
    d = i + t[i] - 1
    if d <= N:
        dp[d] = max(dp[d], dp[i - 1] + p[i])
print(max(dp))
