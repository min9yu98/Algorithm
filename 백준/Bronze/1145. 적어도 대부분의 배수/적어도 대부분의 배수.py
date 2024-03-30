import sys
from itertools import combinations

input = sys.stdin.readline

nums = list(map(int, input().split()))
candidate = []
comb = []
for i in range(3, 6):
    comb += list(combinations(nums, i))
for e in comb:
    e = list(e)
    e.sort()
    for i in range(1, e[-1] ** 2):
        maxi = e[-1] * i
        check = 0
        for j in range(len(e) - 1):
            if maxi % e[j] == 0:
                check += 1
        if check == len(e) - 1:
            candidate.append(maxi)
            break

candidate.sort()
print(candidate[0])
