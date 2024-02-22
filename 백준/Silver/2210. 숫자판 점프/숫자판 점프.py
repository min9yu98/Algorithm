import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(5)]
result = set()
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(x, y, cnt, sen):
    if cnt == 6:
        result.add(sen)
        return
    for i in range(4):
        dx, dy = x + move[i][0], y + move[i][1]
        if 0 <= dx < 5 and 0 <= dy < 5:
            dfs(dx, dy, cnt + 1, sen + str(graph[dy][dx]))


for i in range(5):
    for j in range(5):
        dfs(j, i, 0, '')
print(len(result))
