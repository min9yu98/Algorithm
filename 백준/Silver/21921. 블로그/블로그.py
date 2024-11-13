import sys

input = sys.stdin.readline

n, x = map(int, input().split())
visitors = list(map(int, input().split()))

if sum(visitors) == 0:
    print('SAD')
    exit(0)

sum_v = sum(visitors[0: x])
ans = sum(visitors[0: x])
max_cnt = 1
for i in range(n - x):
    sum_v -= visitors[i]
    sum_v += visitors[i + x]
    if ans <= sum_v:
        if ans == sum_v:
            max_cnt += 1
        else:
            max_cnt = 1
        ans = sum_v

print(ans)
print(max_cnt)
