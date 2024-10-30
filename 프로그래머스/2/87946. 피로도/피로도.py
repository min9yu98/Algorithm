answer = 0

def dfs(k, cnt, dg, visited):
    global answer
    answer = max(answer, cnt)
    for i in range(len(dg)):
        if not visited[i] and k >= dg[i][0]:
            visited[i] = 1
            dfs(k - dg[i][1], cnt + 1, dg, visited)
            visited[i] = 0

def solution(k, dg):
    global answer
    visited = [0] * len(dg)
    dfs(k, 0, dg, visited)
    return answer