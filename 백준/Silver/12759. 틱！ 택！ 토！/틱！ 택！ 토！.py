import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

n = int(input())
board = [[0] * 4 for _ in range(4)]
move = [
    [(1, 1), (1, 2), (1, 3)],
    [(2, 1), (2, 2), (2, 3)],
    [(3, 1), (3, 2), (3, 3)],
    [(1, 1), (2, 2), (3, 3)],
    [(1, 3), (2, 2), (3, 1)],
    [(1, 1), (2, 1), (3, 1)],
    [(1, 2), (2, 2), (3, 2)],
    [(1, 3), (2, 3), (3, 3)]
]
ans = []


def tictactoe(board, player):
    for i in range(8):
        cnt = 0
        for j in range(3):
            mx, my = move[i][j][0], move[i][j][1]
            if board[mx][my] == player:
                cnt += 1
        if cnt == 3:
            return player
    return 0


for i in range(9):
    x, y = map(int, input().split())
    player = 0
    if i % 2 == 0:
        if n == 1:
            player = 1
        else:
            player = 2
    else:
        if n == 1:
            player = 2
        else:
            player = 1
    board[x][y] = player
    ans = tictactoe(board, player)
    if ans != 0:
        break
print(ans)
