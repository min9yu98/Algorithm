import sys
input = sys.stdin.readline

n = int(input())
satisfaction = [int(input()) for _ in range(n)]
satisfaction.sort()
ans = 0
for i in range(n):
    if satisfaction[i] != i + 1:
        ans += abs(satisfaction[i] - (i + 1))
print(ans)
