import sys

input = sys.stdin.readline

N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]


def mul(lst1, lst2):
    n = len(lst1)
    result = [[0] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            tmp = 0
            for i in range(n):
                tmp += lst1[row][i] * lst2[i][col]
            result[row][col] = tmp % 1000
    return result


def square(matx, b):
    if b == 1:
        for x in range(len(matx)):
            for y in range(len(matx)):
                matx[x][y] %= 1000
        return matx
    tmp = square(matx, b // 2)
    if b % 2:
        return mul(mul(tmp, tmp), matx)
    else:
        return mul(tmp, tmp)


ans = square(matrix, B)
for num in ans:
    print(*num)
