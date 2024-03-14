import sys
from copy import deepcopy

input = sys.stdin.readline

n = int(input())
order = [int(input()) for _ in range(n)]
stack = []
ans = []

idx = 1
stack.append(idx)
ans.append("+")
while order:
    if stack:
        if stack[-1] == order[0]:
            ans.append("-")
            order.pop(0)
            stack.pop()
            continue
    if idx < n:
        idx += 1
    stack.append(idx)
    ans.append("+")
    if len(stack) > 2:
        if stack[-1] == stack[-2]:
            ans = ['NO']
            break

for e in ans:
    print(e)
