def solution(board, h, w):
    answer = 0
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    max_h = len(board)
    max_w = len(board[0])
    for dx, dy in move:
        lx, ly = dx + h, dy + w
        if 0 <= lx < max_h and 0 <= ly < max_w:
            if board[h][w] == board[lx][ly]:
                answer += 1
    return answer