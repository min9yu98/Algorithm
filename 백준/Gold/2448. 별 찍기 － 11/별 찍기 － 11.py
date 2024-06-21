import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

n = int(input())
ans = [[" "] * 2 * n for _ in range(n)]


def star(x, y, size):
    if size == 3:
        ans[x][y] = "*"
        ans[x + 1][y - 1] = ans[x + 1][y + 1] = "*"
        for k in range(-2, 3):
            ans[x + 2][y - k] = "*"
    else:
        new_size = size // 2
        star(x, y, new_size)
        star(x + new_size, y - new_size, new_size)
        star(x + new_size, y + new_size, new_size)


star(0, n - 1, n)
for star in ans:
    print("".join(star))
