import sys
_input = sys.stdin.readline

n = int(_input())
s = list(map(int, _input().split()))
v = int(_input())

print(s.count(v))
