import sys
from copy import deepcopy

input = sys.stdin.readline

piece = list(map(int, input().split()))
check = deepcopy(piece)
check.sort()

while piece != check:
    if piece[0] > piece[1]:
        piece[0], piece[1] = piece[1], piece[0]
        print(piece[0], piece[1], piece[2], piece[3], piece[4])
    if piece[1] > piece[2]:
        piece[1], piece[2] = piece[2], piece[1]
        print(piece[0], piece[1], piece[2], piece[3], piece[4])
    if piece[2] > piece[3]:
        piece[2], piece[3] = piece[3], piece[2]
        print(piece[0], piece[1], piece[2], piece[3], piece[4])
    if piece[3] > piece[4]:
        piece[3], piece[4] = piece[4], piece[3]
        print(piece[0], piece[1], piece[2], piece[3], piece[4])
