import sys
input = sys.stdin.readline

n, l = map(int, input().split())
height = list(map(int, input().split()))
height.sort()

for e in height:
    if e <= l:
        l += 1

print(l)
