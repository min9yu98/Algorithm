import sys
input = sys.stdin.readline

n = int(input())
marble = list(map(int, input().split()))
marble.sort()
cnt = 0
for i in range(-1, n - 1):
    cnt += abs(marble[i + 1] - marble[i])
print(cnt)
