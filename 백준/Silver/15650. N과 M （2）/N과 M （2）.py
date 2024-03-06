import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
for e in combinations([i for i in range(1, n + 1)], m):
    print(' '.join(list(map(str, e))))

