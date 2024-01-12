answer = 0
visited = []

def dfs(k, dg, cnt):
    global answer
    if cnt > answer:
        answer = cnt
    for i in range(len(dg)):
        if k >= dg[i][0] and not visited[i]:
            visited[i] = True
            dfs(k - dg[i][1], dg, cnt + 1)
            visited[i] = False


def solution(k, dg):
    global visited
    visited = [False] * len(dg)
    dfs(k, dg, 0)
    return answer
