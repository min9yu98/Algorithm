import sys
from copy import deepcopy

input = sys.stdin.readline

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]
t = sum(lines) // n
start = 1
end = max(lines)
while start <= end:
    mid = (start + end) // 2
    res = 0
    for l in lines:
        res += l // mid
    if res >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
