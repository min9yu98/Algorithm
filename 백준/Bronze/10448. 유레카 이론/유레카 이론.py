import sys
from itertools import combinations

input = sys.stdin.readline

lst = [(i * (i + 1)) // 2 for i in range(1, 46)]
check = [0] * 1001

for i in lst:
    for j in lst:
        for k in lst:
            total = i + j + k
            if total <= 1000:
                check[total] = 1

for _ in range(int(input())):
    k = int(input())
    print(check[k])
