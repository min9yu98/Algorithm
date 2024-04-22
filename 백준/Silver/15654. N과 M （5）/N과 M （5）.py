from itertools import permutations
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
comb = permutations(numbers, m)

for e in comb:
    print(' '.join(list(map(str, e))))
