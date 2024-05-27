import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
start, end = 0, 0
arr.sort(reverse=True)
ans = 20000000001
while n > end >= start:
    if arr[start] - arr[end] >= m:
        ans = min(ans, arr[start] - arr[end])
        start += 1
    else:
        end += 1

print(ans)
