import sys
from copy import deepcopy

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = deepcopy(arr)
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], arr[i] + dp[j])
print(max(dp))

