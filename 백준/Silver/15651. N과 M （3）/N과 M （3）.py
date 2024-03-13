import sys
from itertools import product

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(product(list(range(1, n + 1)), repeat=m))
for num in nums:
    for e in num:
        print(e, end=' ')
    print()
