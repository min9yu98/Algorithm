import sys

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

h, w = map(int, input().split())
blocks = list(map(int, input().split()))
stack = []

for i in range(w):
    if not stack:
        stack.append([blocks[i], i])
    else:
        if blocks[i] > stack[-1][0]:
            stack.append([blocks[i], i])
reverse_stack = []
for i in range(w - 1, -1, -1):
    if not reverse_stack:
        reverse_stack.append([blocks[i], i])
    else:
        if blocks[i] > reverse_stack[-1][0]:
            reverse_stack.append([blocks[i], i])
tmp_stack = stack + reverse_stack
total_stack = list(map(list, set(map(tuple, tmp_stack))))
total_stack.sort(key=lambda x: (x[1], x[0]))

ans = 0
for i in range(len(total_stack) - 1):
    if total_stack[i][0] < total_stack[i + 1][0]:
        for j in range(total_stack[i][1], total_stack[i + 1][1]):
            ans += total_stack[i][0] - blocks[j]
    else:
        for j in range(total_stack[i + 1][1], total_stack[i][1], -1):
            ans += total_stack[i + 1][0] - blocks[j]

print(ans)
