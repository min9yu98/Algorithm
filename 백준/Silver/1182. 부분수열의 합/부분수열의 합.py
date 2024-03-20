import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0


def back(idx, total):
    global cnt
    if total == s:
        cnt += 1
    for i in range(idx + 1, n):
        total += nums[i]
        back(i, total)
        total -= nums[i]


for i in range(n):
    back(i, nums[i])
print(cnt)
