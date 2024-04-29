import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

n, m = map(int, input().split())
tree = [[] for _ in range(n + 1)]
cnt = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(n - 1):
    node1, node2, l = map(int, input().split())
    tree[node1].append(node2)
    cnt[node1][node2] = l
    tree[node2].append(node1)
    cnt[node2][node1] = l


def dfs(x, y, s):
    visited[x] = 1
    if x == y:
        print(s)
        return
    for node in tree[x]:
        if not visited[node]:
            dfs(node, y, s + cnt[node][x])


for _ in range(m):
    a, b = map(int, input().split())
    visited = [0] * (n + 1)
    dfs(a, b, 0)
