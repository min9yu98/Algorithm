import sys
input = sys.stdin.readline

n = int(input())
exp = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
result = 2147000000


def dfs(l, idx):
    global result
    if l == n // 2:
        a, b = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    a += exp[i][j]
                elif not visited[i] and not visited[j]:
                    b += exp[i][j]
        result = min(result, abs(a - b))
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(l + 1, i + 1)
            visited[i] = False

            
dfs(0, 0)
print(result)
