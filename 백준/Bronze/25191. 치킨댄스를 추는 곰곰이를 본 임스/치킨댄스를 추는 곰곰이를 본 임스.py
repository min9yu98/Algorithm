import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
total = a // 2 + b
print(total if n >= a // 2 + b else n)
