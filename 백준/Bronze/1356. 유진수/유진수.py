import sys
from itertools import combinations

input = sys.stdin.readline


def mul(lst):
    total = 1
    for e in lst:
        total *= int(e)
    return total


n = list(input().strip())
if len(n) == 1:
    print('NO')
    exit(0)
flag = False
for i in range(len(n)):
    if mul(n[:i]) == mul(n[i:]):
        print('YES')
        flag = True
        break
if not flag:
    print('NO')

