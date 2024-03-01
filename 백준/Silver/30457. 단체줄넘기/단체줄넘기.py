import sys
input = sys.stdin.readline

n = int(input())
people = list(map(int, input().split()))
lst = [0] * 1001
for e in people:
    lst[e] += 1
for e in set(people):
    if lst[e] > 2:
        n -= lst[e] - 2
print(n)
