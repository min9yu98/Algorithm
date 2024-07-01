import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

S = list(input().strip())
T = list(input().strip())


def dfs(t):
    if t == S:
        print(1)
        exit()
    if len(t) == 0:
        return 0
    if t[-1] == 'A':
        dfs(t[:-1])
    if t[0] == 'B':
        dfs(t[1:][::-1])


dfs(T)
print(0)
