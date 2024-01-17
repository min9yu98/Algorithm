import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

lst.sort()
total = 0
for i in range(len(lst)):
    total += lst[i] * sum(lst[i + 1:])
print(total)
