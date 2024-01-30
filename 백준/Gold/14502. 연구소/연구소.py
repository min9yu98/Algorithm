from itertools import combinations
from copy import deepcopy
from collections import deque
import sys

input = sys.stdin.readline
move_x = [0, 0, -1, 1]
move_y = [1, -1, 0, 0]


# bfs에서 이미 벽을 쌓은 t_graph안에 바이러스를 확산시킨 후 0의 갯수 카운트 및 max값 갱신
def bfs(t_graph):
    global answer
    queue = deque([(j, i) for j in range(m) for i in range(n) if t_graph[i][j] == 2])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx = x + move_x[i]
            dy = y + move_y[i]
            if 0 <= dx < m and 0 <= dy < n and not t_graph[dy][dx]:
                t_graph[dy][dx] = 2
                queue.append((dx, dy))
    cnt = sum([e.count(0) for e in t_graph])
    answer = max(answer, cnt)


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
tmp_wall_graph = [(x, y) for x in range(m) for y in range(n) if not graph[y][x]]  # 벽을 쌓을 수 있는 공간
answer = 0

# 그래프 별로 벽을 조합에 따라 세운 후 그 그래프를 bfs 적용
for comb in combinations(tmp_wall_graph, 3):  # 3개의 벽을 쌓기 위해 모든 벽을 쌓을 수 있는 공간에서 3부분만 조합한 후 반복문 실행
    tmp_graph = deepcopy(graph)
    for x, y in comb:
        tmp_graph[y][x] = 1
    bfs(tmp_graph)

print(answer)
