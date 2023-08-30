import sys

input = sys.stdin.readline

n, x = map(int, input().split())
visitors = list(map(int, input().split()))
max_visit = 0
max_visit_count = 1

if max(visitors) == 0:
    print("SAD")
    exit(0)

max_visit = sum(visitors[0:x])
sum_visitors = sum(visitors[0:x])
for i in range(n - x):
    sum_visitors -= visitors[i]
    sum_visitors += visitors[i + x]
    if sum_visitors >= max_visit:
        if sum_visitors == max_visit:
            max_visit_count += 1
        else:
            max_visit_count = 1
        max_visit = sum_visitors

print(max_visit)
print(max_visit_count)

