import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

n, r, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
cnt = [0] * (n + 1)
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def tree(current):
    cnt[current] += 1
    for node in graph[current]:
        if not cnt[node]:
            tree(node)
            cnt[current] += cnt[node]


tree(r)
for _ in range(q):
    u = int(input())
    print(cnt[u])

