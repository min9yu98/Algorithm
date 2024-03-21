import sys

input = sys.stdin.readline

s = input().strip()
slicing = len(s) // 10 + (1 if len(s) % 10 else 0)
for i in range(slicing):
    print(s[10 * i: 10 * (i + 1)])

