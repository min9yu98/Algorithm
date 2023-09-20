import sys

n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
check = [0] * (max(lst) + 1)
result = 0
i, j = 0, 0

while j < n:
    if check[lst[j]] < m:
        check[lst[j]] += 1
        j += 1
    else:
        check[lst[i]] -= 1
        i += 1

    result = max(result, j - i)

print(result)