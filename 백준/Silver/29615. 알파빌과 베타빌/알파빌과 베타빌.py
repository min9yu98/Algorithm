import sys
input = sys.stdin.readline

n, m = map(int, input().split())
waiting = list(map(int, input().split()))
friends = list(map(int, input().split()))
order = waiting[:m]
cnt = 0
for e in order:
    if e not in friends:
        cnt += 1
print(cnt)
