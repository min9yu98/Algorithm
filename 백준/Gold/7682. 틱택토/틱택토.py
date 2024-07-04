import sys

input = sys.stdin.readline

move = [(0, 1), (1, 0), (1, 1), (1, -1)]


def dfs(s, x, y, move_idx, cnt):
    if cnt == 2:
        return True
    result = False
    mx, my = x + move[move_idx][0], y + move[move_idx][1]
    if 0 <= mx < 3 and 0 <= my < 3:
        if board[mx][my] == s:
            result = dfs(s, mx, my, move_idx, cnt + 1)
            if result:
                return result
    return result


while True:
    board = []
    tmp = input().strip()
    if tmp == 'end':
        break
    tmp_board = list(tmp)

    x_count, o_count, p_count = tmp_board.count('X'), tmp_board.count('O'), tmp_board.count('.')

    if x_count < o_count:
        print('invalid')
        continue
    if abs(x_count - o_count) >= 2:
        print('invalid')
        continue
    if x_count < 3 and o_count < 3:
        print('invalid')
        continue

    for i in range(0, 9, 3):
        board.append([tmp_board[i], tmp_board[i + 1], tmp_board[i + 2]])

    x_idx_lst, o_idx_lst = [], []
    for i in range(3):
        if board[0][i] == 'X':
            x_idx_lst.append([0, i])
        elif board[0][i] == 'O':
            o_idx_lst.append([0, i])
    for i in range(1, 3):
        if board[i][0] == 'X':
            x_idx_lst.append([i, 0])
        elif board[i][0] == 'O':
            o_idx_lst.append([i, 0])

    x_check, o_check = False, False
    for i in range(len(x_idx_lst)):
        for j in range(4):
            x_check = dfs('X', x_idx_lst[i][0], x_idx_lst[i][1], j, 0)
            if x_check:
                break
        if x_check:
            break
    for i in range(len(o_idx_lst)):
        for j in range(4):
            o_check = dfs('O', o_idx_lst[i][0], o_idx_lst[i][1], j, 0)
            if o_check:
                break
        if o_check:
            break
    if x_check and o_check:
        print('invalid')
        continue
    if not x_check and not o_check:
        if p_count != 0:
            print('invalid')
            continue
    if x_check:
        if x_count <= o_count:
            print('invalid')
            continue
    if o_check:
        if x_count > o_count:
            print('invalid')
            continue
    print('valid')
