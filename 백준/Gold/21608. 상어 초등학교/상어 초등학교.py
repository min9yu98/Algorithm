import sys
from collections import deque

input = sys.stdin.readline

near_x = [0, 0, -1, 1]
near_y = [1, -1, 0, 0]

n = int(input())
arr = [[0] * n for _ in range(n)]
students = [list(map(int, input().split())) for _ in range(n ** 2)]

for order in range(n ** 2):
    student = students[order]
    tmp = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                like = 0
                blank = 0
                for k in range(4):
                    dx, dy = j + near_x[k], i + near_y[k]
                    if 0 <= dx < n and 0 <= dy < n:
                        if arr[dy][dx] in student[1:]:
                            like += 1
                        if arr[dy][dx] == 0:
                            blank += 1
                tmp.append([like, blank, i, j])
    tmp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    arr[tmp[0][2]][tmp[0][3]] = student[0]
result = 0
students.sort()
for i in range(n):
    for j in range(n):
        ans = 0
        for k in range(4):
            nx, ny = j + near_x[k], i + near_y[k]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[ny][nx] in students[arr[i][j] - 1]:
                    ans += 1
        if ans != 0:
            result += 10 ** (ans - 1)
print(result)
