import sys

input = sys.stdin.readline

m, n = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()


def calc(x):
    cnt = 0
    for e in arr:
        if e - x < 0:
            continue
        else:
            cnt += e // x
    return cnt


start, end = 1, arr[-1]
while start <= end:
    mid = (start + end) // 2
    if calc(mid) < m:
        end = mid - 1
    else:
        start = mid + 1
print(end)
