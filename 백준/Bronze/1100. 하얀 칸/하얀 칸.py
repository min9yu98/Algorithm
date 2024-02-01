import sys
input = sys.stdin.readline

chess = [list(input().strip()) for _ in range(8)]
answer = 0
for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0:
            if chess[i][j] == 'F':
                answer += 1
        elif i % 2 == 1 and j % 2 == 1:
            if chess[i][j] == 'F':
                answer += 1
print(answer)
