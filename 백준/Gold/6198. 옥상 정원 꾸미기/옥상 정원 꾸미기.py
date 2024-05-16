import sys
from copy import deepcopy

input = sys.stdin.readline

n = int(input())
buildings = [int(input()) for _ in range(n)]
stack = []
ans = 0

for i in range(n):
    while stack and stack[-1] <= buildings[i]:
        stack.pop()
    stack.append(buildings[i])
    ans += len(stack) - 1
print(ans)
