import sys
from copy import deepcopy

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack = []
ans = []
for i in range(n):
    while stack:
        if stack[-1][0] < arr[i]:
            stack.pop()
        else:
            ans.append(stack[-1][1] + 1)
            break
    if not stack:
        ans.append(0)
    stack.append([arr[i], i])
print(" ".join(map(str, ans)))
