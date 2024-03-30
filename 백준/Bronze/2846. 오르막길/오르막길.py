import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
height = list(map(int, input().split()))

dif = 0

for i in range(n):
    tmp = height[i]
    for j in range(i + 1, n):
        if tmp < height[j]:
            tmp = height[j]
            dif = max(dif, height[j] - height[i])
        else:
            break
print(dif)
