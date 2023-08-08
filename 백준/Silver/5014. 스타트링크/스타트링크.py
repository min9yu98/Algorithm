from collections import deque
import sys


def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        if v == g:
            return arr[v]
        for e in (v + u, v - d):
            if 0 < e <= f and not visited[e]:
                visited[e] = True
                arr[e] = arr[v] + 1
                queue.append(e)
    if arr[g] == 0:
        return "use the stairs"


f, s, g, u, d = map(int, sys.stdin.readline().split())
arr = [0] * (f + 1)
visited = [False] * (f + 1)
print(bfs(s))