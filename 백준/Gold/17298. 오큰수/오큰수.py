import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack = []
ans = []

for i in range(n - 1, -1, -1):
    while stack:
        if stack[-1] > arr[i]:
            ans.append(stack[-1])
            stack.append(arr[i])
            break
        else:
            stack.pop()
    if not stack:
        ans.append(-1)
        stack.append(arr[i])
ans.reverse()
print(' '.join(map(str, ans)))
