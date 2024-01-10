import sys

input = sys.stdin.readline

n, m = map(int, input().split())
box = list(map(int, input().split()))
if n == 0:
    print(n)
else:
    result = 0
    tmp = 0
    idx = 0
    while idx < n:
        tmp += box[idx]
        if tmp > m:
            result += 1
            tmp = 0
        elif tmp == m:
            result += 1
            tmp = 0
            idx += 1
        else:
            idx += 1
            continue
    if tmp != 0:
        result += 1
    print(result)
