import sys
input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))
t.sort(reverse=True)
day = 1
for i in range(n):
    t[i] -= n - i
day += max(t) + n + 1
print(day)