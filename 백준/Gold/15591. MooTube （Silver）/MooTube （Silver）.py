import sys
from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().split())
rel = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    p, q, r = map(int, input().split())
    rel[p].append([q, r])
    rel[q].append([p, r])


def bfs(movie, criteria):
    cnt = 0
    queue = deque([])
    queue.append(movie)
    visited[movie] = 1
    while queue:
        current_movie = queue.popleft()
        for next_movie, weight in rel[current_movie]:
            if not visited[next_movie]:
                if criteria <= weight:
                    queue.append(next_movie)
                    visited[next_movie] = 1
                    cnt += 1
    return cnt


for _ in range(Q):
    c, m = map(int, input().split())
    visited = [0] * (N + 1)
    print(bfs(m, c))
