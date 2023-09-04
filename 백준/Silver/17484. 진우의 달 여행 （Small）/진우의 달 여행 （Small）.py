import sys

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
move = [(-1, 1), (0, 1), (1, 1)]  # (x, y)


def dp(x, y, move_idx, min_cnt, cnt):
    if y == n - 1:
        return min(min_cnt, cnt)
    for i in range(3):  # len(move)
        if i != move_idx:
            X, Y = x + move[i][0], y + move[i][1]
            if 0 <= X < m and 0 <= Y < n:
                min_cnt = dp(X, Y, i, min_cnt, cnt + graph[Y][X])
    return min_cnt


min_fuel = int(sys.maxsize)
for i in range(m):
    for j in range(3):
        min_fuel = min(dp(i, 0, j, min_fuel, graph[0][i]), min_fuel)
print(min_fuel)
