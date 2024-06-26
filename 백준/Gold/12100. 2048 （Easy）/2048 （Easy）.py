import sys
import copy

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = []


# 보드를 특정 방향으로 슬라이딩하고 합치는 함수
def slide_combine(board, direction):
    new_board = copy.deepcopy(board)
    merged = [[False] * n for _ in range(n)]
    
    if direction == 1:  # 하 -> 상
        for col in range(n):
            for row in range(1, n):
                if new_board[row][col] != 0:
                    r = row
                    while r > 0 and new_board[r-1][col] == 0:
                        new_board[r-1][col] = new_board[r][col]
                        new_board[r][col] = 0
                        r -= 1
                    if r > 0 and new_board[r-1][col] == new_board[r][col] and not merged[r-1][col]:
                        new_board[r-1][col] *= 2
                        new_board[r][col] = 0
                        merged[r-1][col] = True

    elif direction == 2:  # 상 -> 하
        for col in range(n):
            for row in range(n-2, -1, -1):
                if new_board[row][col] != 0:
                    r = row
                    while r < n-1 and new_board[r+1][col] == 0:
                        new_board[r+1][col] = new_board[r][col]
                        new_board[r][col] = 0
                        r += 1
                    if r < n-1 and new_board[r+1][col] == new_board[r][col] and not merged[r+1][col]:
                        new_board[r+1][col] *= 2
                        new_board[r][col] = 0
                        merged[r+1][col] = True

    elif direction == 3:  # 좌 -> 우
        for row in range(n):
            for col in range(n-2, -1, -1):
                if new_board[row][col] != 0:
                    c = col
                    while c < n-1 and new_board[row][c+1] == 0:
                        new_board[row][c+1] = new_board[row][c]
                        new_board[row][c] = 0
                        c += 1
                    if c < n-1 and new_board[row][c+1] == new_board[row][c] and not merged[row][c+1]:
                        new_board[row][c+1] *= 2
                        new_board[row][c] = 0
                        merged[row][c+1] = True

    elif direction == 4:  # 우 -> 좌
        for row in range(n):
            for col in range(1, n):
                if new_board[row][col] != 0:
                    c = col
                    while c > 0 and new_board[row][c-1] == 0:
                        new_board[row][c-1] = new_board[row][c]
                        new_board[row][c] = 0
                        c -= 1
                    if c > 0 and new_board[row][c-1] == new_board[row][c] and not merged[row][c-1]:
                        new_board[row][c-1] *= 2
                        new_board[row][c] = 0
                        merged[row][c-1] = True

    return new_board


def find_max(board):
    return max(max(row) for row in board)


def dfs(board, depth):
    if depth == 5:
        ans.append(find_max(board))
        return

    for direction in range(1, 5):
        new_board = slide_combine(board, direction)
        dfs(new_board, depth + 1)


dfs(board, 0)
print(max(ans))
