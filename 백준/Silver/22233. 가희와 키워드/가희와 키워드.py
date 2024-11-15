import sys

input = sys.stdin.readline

n, m = map(int, input().split())
memo = {input().strip() : 1 for _ in range(n)}
tmp = n
for _ in range(m):
    lst = input().strip().split(',')
    for e in lst:
        if e in memo.keys():
            if memo[e] == 1:
                memo[e] -= 1
                tmp -= 1
    print(tmp)
