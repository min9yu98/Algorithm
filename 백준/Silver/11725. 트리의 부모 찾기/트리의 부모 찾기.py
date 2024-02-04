from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
answer = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
while queue:
    k = queue.popleft()
    visited[k] = 1
    for e in graph[k]:
        if not visited[e]:
            answer[e] = k
            visited[e] = 1
            queue.append(e)
for num in answer[2:]:
    print(num)
