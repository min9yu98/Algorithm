import sys

input = sys.stdin.readline

n, m = map(int, input().split())
alpha = {}
for i in range(n):
    s = input().strip()
    if not alpha.get(s):
        alpha[s] = 1
    else:
        alpha[s] += 1
lst = sorted(alpha.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for e in lst:
    if len(e[0]) >= m:
        print(e[0])
