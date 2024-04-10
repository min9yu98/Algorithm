import sys
from copy import deepcopy

input = sys.stdin.readline

scores = [int(input()) for _ in range(8)]
tmp = deepcopy(scores)
tmp.sort()
print(sum(tmp[3:]))

for i in range(8):
    for n in tmp[3:]:
        if scores[i] == n:
            print(i + 1, end=" ")
            break
