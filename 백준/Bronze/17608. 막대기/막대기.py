import sys

input = sys.stdin.readline

n = int(input())
sticks = [int(input()) for _ in range(n)]
sticks.reverse()
maxi = sticks[0]
cnt = 1
for stick in sticks:
    if maxi < stick:
        maxi = stick
        cnt += 1
print(cnt)
