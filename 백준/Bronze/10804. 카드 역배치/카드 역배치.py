import sys
from collections import deque

input = sys.stdin.readline

lst = [i for i in range(1, 21)]

for _ in range(10):
    a, b = map(int, input().split())
    lst[a - 1: b] = reversed(lst[a - 1: b])
print(' '.join(map(str, lst)))
