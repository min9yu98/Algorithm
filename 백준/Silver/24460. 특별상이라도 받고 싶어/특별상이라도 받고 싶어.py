import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


def recur(x, y, size):
    if size == 2:
        return sorted([arr[x][y], arr[x + 1][y], arr[x][y + 1], arr[x + 1][y + 1]])[1]
    newSize = size // 2
    return sorted([recur(x, y, newSize), recur(x, y + newSize, newSize), recur(x + newSize, y, newSize), recur(x + newSize, y + newSize, newSize)])[1]


if n == 1:
    print(arr[0][0])
else:
    print(recur(0, 0, n))
