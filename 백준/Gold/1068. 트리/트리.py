import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n)]
visited = [False] * n
root = 0
ans = 0

for node, parent in enumerate(map(int, input().split())):
    if parent == -1:
        root = node
    else:
        tree[parent].append(node)

deleted = int(input())
visited[deleted] = True


def dfs(x):
    global ans
    if visited[x]:
        return
    visited[x] = True
    if len(tree[x]) == 0:
        ans += 1
        return
    elif len(tree[x]) == 1 and tree[x][0] == deleted:
        ans += 1
    for s in tree[x]:
        dfs(s)


dfs(root)
print(ans)
