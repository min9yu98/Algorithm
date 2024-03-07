import sys
from collections import deque
input = sys.stdin.readline

knight = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (2, 1), (1, 2)]

for _ in range(int(input())):
    l = int(input())
    cur_x, cur_y = map(int, input().split())
    fut_x, fut_y = map(int, input().split())
    visited = [[0] * l for _ in range(l)]
    visited[cur_y][cur_x] = 1
    flag = False
    queue = deque([(cur_x, cur_y)])
    while queue:
        x, y = queue.popleft()
        for lx, ly in knight:
            dx, dy = lx + x, ly + y
            if 0 <= dx < l and 0 <= dy < l:
                if not visited[dy][dx]:
                    visited[dy][dx] = visited[y][x] + 1
                    queue.append((dx, dy))
                    if dx == fut_x and dy == fut_y:
                        flag = True
                        break
        if flag:
            break
    print(visited[fut_y][fut_x] - 1)
