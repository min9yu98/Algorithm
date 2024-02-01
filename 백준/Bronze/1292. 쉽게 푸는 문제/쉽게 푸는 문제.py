import sys
input = sys.stdin.readline

a, b = map(int, input().split())
lst = []
for i in range(1, 1001):
    lst += [i] * i
print(sum(lst[a - 1:b]))
