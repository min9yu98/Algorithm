import sys

input = sys.stdin.readline

n, m = map(int, input().split())
if n == 0:
    print(n)
else:
    box = list(map(int, input().split()))
    result = 1
    tmp = 0
    for i in range(len(box)):
        if box[i] + tmp <= m:
            tmp += box[i]
        else:
            result += 1
            tmp = box[i]
    print(result)
