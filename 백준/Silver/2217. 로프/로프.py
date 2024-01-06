import sys
input = sys.stdin.readline

n = int(input())
rope = [int(input()) for _ in range(n)]
rope.sort()

weight = []
for r in rope:
    weight.append(r * n)
    n -= 1
print(max(weight))
