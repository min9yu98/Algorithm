import sys
from itertools import combinations

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split(",")))

b = []
for _ in range(k):
    for i in range(len(a) - 1):
        b.append(a[i + 1] - a[i])
    a = b
    b = []
if not b:
    print(','.join(list(map(str, a))))
else:
    print(','.join(list(map(str, b))))
