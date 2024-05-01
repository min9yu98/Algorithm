import sys
from collections import deque

input = sys.stdin.readline


queue = deque([])

for _ in range(int(input())):
    s = input().strip().split()
    if len(s) == 2:
        if s[0] == "push":
            queue.append(s[1])
    else:
        if s[0] == "front":
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif s[0] == "back":
            if queue:
                print(queue[-1])
            else:
                print(-1)
        elif s[0] == "empty":
            if not queue:
                print(1)
            else:
                print(0)
        elif s[0] == "size":
            print(len(queue))
        elif s[0] == "pop":
            if queue:
                print(queue.popleft())
            else:
                print(-1)

