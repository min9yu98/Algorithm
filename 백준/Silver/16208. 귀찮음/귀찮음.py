import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

lst.sort()
answer = 0
total = sum(lst)
for e in lst:
    answer += e * (total - e)
    total -= e
print(answer)
