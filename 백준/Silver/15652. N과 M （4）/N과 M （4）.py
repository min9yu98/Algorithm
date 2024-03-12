import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
lst = []


def dfs(cnt, idx):
    if cnt == m:
        print(' '.join(map(str, lst)))
        return
    for i in range(idx, n + 1):
        lst.append(i)
        dfs(cnt + 1, i)
        lst.pop()


dfs(0, 1)
