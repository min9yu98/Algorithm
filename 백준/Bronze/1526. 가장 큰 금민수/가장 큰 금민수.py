import sys

input = sys.stdin.readline

n = int(input())
for i in range(n, 0, -1):
    s = str(i)
    if s.count('7') + s.count('4') == len(s):
        print(s)
        break
