from collections import deque

def bfs(n, computers, visited, idx):
    queue = deque([idx])
    while queue:
        computer = queue.popleft()
        visited[computer] = True
        for i in range(n):
            if computer != i and computers[computer][i] == 1:
                if not visited[i]:
                    queue.append(i)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            bfs(n, computers, visited, i)
            answer += 1
    return answer