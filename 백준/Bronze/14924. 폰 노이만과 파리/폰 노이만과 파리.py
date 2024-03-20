import sys

input = sys.stdin.readline

s, t, d = map(int, input().split())
print(t * (d // (s * 2)))
