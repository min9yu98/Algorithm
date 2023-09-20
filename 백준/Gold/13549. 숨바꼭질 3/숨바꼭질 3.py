from collections import deque

n, k = map(int, input().split())
queue = deque()
queue.append(n)
visited = [-1] * 100001
visited[n] = 0

while queue:
    num = queue.popleft()
    if num == k:
        print(visited[num])
        break
    if 0 <= num - 1 < 100001 and visited[num - 1] == -1:
        visited[num - 1] = visited[num] + 1
        queue.append(num - 1)
    if 0 < num * 2 < 100001 and visited[num * 2] == -1:
        visited[num * 2] = visited[num]
        queue.appendleft(num * 2)
    if 0 <= num + 1 < 100001 and visited[num + 1] == -1:
        visited[num + 1] = visited[num] + 1
        queue.append(num + 1)
 
