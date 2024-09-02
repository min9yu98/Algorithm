import sys

input = sys.stdin.readline

while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    n = lst[0]
    max_area = 0
    stack = []
    for i in range(1, n + 1):
        if len(stack) == 0:
            stack.append((i, lst[i]))
        else:
            if stack[-1][1] <= lst[i]:
                stack.append((i, lst[i]))
            else:
                while len(stack) > 0 and stack[-1][1] > lst[i]:
                    rm = stack.pop()
                    if len(stack) == 0:
                        width = i - 1
                    else:
                        width = i - stack[-1][0] - 1
                    max_area = max(max_area, rm[1] * width)
                stack.append((i, lst[i]))
    while stack:
        rm = stack.pop()
        if len(stack) == 0:
            width = n
        else:
            width = (n - stack[-1][0])
        max_area = max(max_area, rm[1] * width)
    print(max_area)
