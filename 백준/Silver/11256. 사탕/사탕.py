import sys
input = sys.stdin.readline

for _ in range(int(input())):
    j, n = map(int, input().split())
    boxes = []
    visited = [False] * n
    cnt = 0
    for _ in range(n):
        a, b = map(int, input().split())
        boxes.append(a * b)
    boxes.sort(reverse=True)
    for b in boxes:
        j -= b
        cnt += 1
        if j <= 0:
            print(cnt)
            break
