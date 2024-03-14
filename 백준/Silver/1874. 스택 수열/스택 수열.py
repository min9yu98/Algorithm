import sys
from copy import deepcopy

input = sys.stdin.readline

n = int(input())
stack = []
ans = []
idx = 1
flag = True

for _ in range(n):
    num = int(input())
    while idx <= num:
        stack.append(idx)
        ans.append("+")
        idx += 1
    if stack[-1] == num:
        stack.pop()
        ans.append("-")
    else:
        flag = False
        break
if flag:
    for e in ans:
        print(e)
else:
    print("NO")
