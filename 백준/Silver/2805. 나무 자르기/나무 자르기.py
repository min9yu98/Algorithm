import sys
from copy import deepcopy

input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()
start = 1
end = tree[-1]


def calc(mid):
    total = 0
    for e in tree:
        if e - mid <= 0:
            continue
        else:
            total += (e - mid)
    return total


while start <= end:
    mid = (start + end) // 2
    if calc(mid) >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
