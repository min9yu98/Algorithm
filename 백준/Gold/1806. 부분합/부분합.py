import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 1e9
total = 0
start, end = 0, 0

while True:
    if total >= m:
        cnt = min(cnt, end - start)
        total -= arr[start]
        start += 1
    elif end == n:
        break
    else:
        total += arr[end]
        end += 1

if cnt == 1e9:
    print(0)
else:
    print(cnt)
