import sys

n = int(sys.stdin.readline())
budget = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline())

start, end = 0, max(budget)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for e in budget:
        if e > mid:
            total += mid
        else:
            total += e
    if total <= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
