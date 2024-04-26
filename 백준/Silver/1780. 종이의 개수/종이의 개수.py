import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = {-1: 0, 0: 0, 1: 0}


def recursion(x, y, n):
    curr = graph[y][x]

    for i in range(y, y + n):
        for j in range(x, x + n):
            if graph[i][j] != curr:
                next = n // 3
                recursion(x, y, next)
                recursion(x, y + next, next)
                recursion(x, y + (next * 2), next)
                recursion(x + next, y, next)
                recursion(x + next, y + next, next)
                recursion(x + next, y + (next * 2), next)
                recursion(x + (next * 2), y, next)
                recursion(x + (next * 2), y + next, next)
                recursion(x + (next * 2), y + (next * 2), next)
                return
    ans[curr] += 1
    return


recursion(0, 0, n)

for i in ans.values():
    print(i)
