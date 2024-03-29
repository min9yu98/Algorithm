import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(n)]
    score.sort()
    top = 0
    result = 1
    for i in range(1, n):
        if score[i][1] < score[top][1]:
            top = i
            result += 1
    print(result)