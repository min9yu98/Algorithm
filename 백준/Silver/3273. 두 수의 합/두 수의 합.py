import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())

start, end = 0, n - 1
cnt = 0
while start < end:
    summ = nums[start] + nums[end]
    if summ > x:
        end -= 1
    elif summ < x:
        start += 1
    elif summ == x:
        cnt += 1
        start += 1
print(cnt)
