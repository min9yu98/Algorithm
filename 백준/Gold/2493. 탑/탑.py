from copy import deepcopy
import sys

input = sys.stdin.readline

n = int(input())
tops = list(map(int, input().split()))
stack = []
ans = []

for i in range(n):
    while stack:
        if tops[i] > stack[-1][1]:
            stack.pop()
        else:
            ans.append(stack[-1][0] + 1)
            break
    if not stack:
        ans.append(0)
    stack.append([i, tops[i]])
print(" ".join(map(str, ans)))
