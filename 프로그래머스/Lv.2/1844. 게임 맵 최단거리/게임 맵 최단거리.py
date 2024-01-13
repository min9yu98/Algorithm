from collections import deque

def solution(maps):
    len_x, len_y = len(maps[0]), len(maps)
    if len_x == 1 and len_y == 1:
        return 1
    move_x = [1, -1, 0, 0]
    move_y = [0, 0, 1, -1]
    visited = [[False] * len_x for _ in range(len_y)]
    queue = deque()
    queue.append((0, 0))
    while queue:
        lx, ly = queue.popleft()
        visited[ly][lx] = True
        for i in range(4):
            dx = lx + move_x[i]
            dy = ly + move_y[i]
            if 0 <= dx < len_x and 0 <= dy < len_y and maps[dy][dx] == 1:
                if not visited[dy][dx]:
                    queue.append((dx, dy))
                    visited[dy][dx] = True
                    maps[dy][dx] = maps[ly][lx] + 1
    answer = maps[len_y - 1][len_x - 1]
    return answer if answer != 1 else -1
