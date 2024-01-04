import sys
from collections import deque
_input = sys.stdin.readline

n, m, v = map(int, _input().split())
rep = [[] for _ in range(n + 1)]
visited_dfs = [False for _ in range(n + 1)]
visited_bfs = [False for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, _input().split())
    rep[a].append(b)
    rep[a].sort()
    rep[b].append(a)
    rep[b].sort()
result_dfs = []
result_bfs = []


def dfs(next_item):
    if visited_dfs[next_item]:
        return
    result_dfs.append(str(next_item))
    visited_dfs[next_item] = True
    for e in rep[next_item]:
        if not visited_dfs[e]:
            dfs(e)
    return

def bfs(start):
    visited_bfs[start] = True
    queue = deque([start])
    while queue:
        vt = queue.popleft()
        result_bfs.append(str(vt))
        for e in rep[vt]:
            if not visited_bfs[e]:
                queue.append(e)
                visited_bfs[e] = True
    return


dfs(v)
bfs(v)

print(' '.join(result_dfs))
print(' '.join(result_bfs))
