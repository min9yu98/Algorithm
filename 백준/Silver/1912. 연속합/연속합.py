import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
maxi = -1001
for i in range(1, n):
    nums[i] = max(nums[i], nums[i] + nums[i - 1])
print(max(nums))
