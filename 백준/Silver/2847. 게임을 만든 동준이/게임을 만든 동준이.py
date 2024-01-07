import sys
input = sys.stdin.readline

n = int(input())
score = [int(input()) for _ in range(n)]

if n == 1:
    print(0)
else:
    result = 0
    for i in range(1, n):
        if score[i - 1] >= score[i]:
            result += score[i - 1] - score[i] + 1
            score[i - 1] = score[i] - 1
    for i in range(n - 1, 0, -1):
        if score[i - 1] >= score[i]:
            result += score[i - 1] - score[i] + 1
            score[i - 1] = score[i] - 1
    print(result)
