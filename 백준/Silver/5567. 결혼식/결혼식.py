import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
relations = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)


def bfs(x):
    queue = deque([x])
    visited[x] = 1
    while queue:
        person = queue.popleft()
        for friend in relations[person]:
            if not visited[friend]:
                visited[friend] = visited[person] + 1
                queue.append(friend)


ans = 0
bfs(1)
for i in range(2, n + 1):
    if 0 < visited[i] <= 3:
        ans += 1
print(ans)

