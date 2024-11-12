import sys

input = sys.stdin.readline

n = int(input())
budgets = list(map(int, input().split()))
m = int(input())

budgets.sort()

start, end = 0, budgets[-1]
while start <= end:
    middle = (start + end) // 2
    tmp = 0
    for b in budgets:
        if b <= middle:
            tmp += b
        else:
            tmp += middle
    if tmp > m:
        end = middle - 1
    else:
        start = middle + 1
print(end)
