import sys
from itertools import product

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
prefixSum = [0] * (n + 1)
prefixSum[1] = nums[0]
for i in range(1, n):
    prefixSum[i + 1] = prefixSum[i] + nums[i]
for _ in range(m):
    a, b = map(int, input().split())
    print(prefixSum[b] - prefixSum[a - 1])
