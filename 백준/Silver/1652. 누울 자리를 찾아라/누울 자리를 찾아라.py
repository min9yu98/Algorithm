import sys

input = sys.stdin.readline

n = int(input())
room = []
for _ in range(n):
    m = list(input().strip())
    room.append(m)
garo_cnt, sero_cnt = 0, 0

for i in range(n):
    tmp_garo, tmp_sero = 0, 0
    for j in range(n):
        if room[i][j] == '.':
            tmp_garo += 1
        else:
            if tmp_garo >= 2:
                garo_cnt += 1
            tmp_garo = 0
        if room[j][i] == '.':
            tmp_sero += 1
        else:
            if tmp_sero >= 2:
                sero_cnt += 1
            tmp_sero = 0
    if tmp_garo >= 2:
        garo_cnt += 1
    if tmp_sero >= 2:
        sero_cnt += 1

print(garo_cnt, sero_cnt)
