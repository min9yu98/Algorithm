from collections import deque
import sys


def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return arr[v]
        for next in (v + 1, v - 1, v * 2):
            if 0 <= next < MAX and not arr[next]:
                arr[next] = arr[v] + 1
                q.append(next)


MAX = 100001
n, k = map(int, sys.stdin.readline().split())
arr = [0] * MAX
print(bfs(n))