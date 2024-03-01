import sys
input = sys.stdin.readline

n = int(input())
waiting = [int(input()) for _ in range(n)]
waiting.sort(reverse=True)
benefit = 0
for i in range(n):
    if waiting[i] - i > 0:
        benefit += waiting[i] - i
print(benefit)
