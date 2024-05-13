import sys

input = sys.stdin.readline

n = int(input())
plus = []
minus = []
ans = 0
for _ in range(n):
    x = int(input())
    if x > 1:
        plus.append(x)
    elif x <= 0:
        minus.append(x)
    else:
        ans += x
plus.sort(reverse=True)
minus.sort()

for i in range(0, len(plus), 2):
    if i + 1 >= len(plus):
        ans += plus[i]
    else:
        ans += plus[i] * plus[i + 1]
for i in range(0, len(minus), 2):
    if i + 1 >= len(minus):
        ans += minus[i]
    else:
        ans += minus[i] * minus[i + 1]
print(ans)
