import sys

input = sys.stdin.readline

mushroom = [int(input()) for _ in range(10)]

cnt = 0
mini = 1001
for i in range(10):
    cnt += mushroom[i]
    if mini >= abs(100 - cnt):
        mini = abs(100 - cnt)
        ans = cnt
print(ans)
