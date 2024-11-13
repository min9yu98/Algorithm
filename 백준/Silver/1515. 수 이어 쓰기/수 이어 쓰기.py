import sys

input = sys.stdin.readline

n = list(input().strip())
num, idx = 0, 0
while True:
    num += 1
    for s in str(num):
        if n[idx] == s:
            idx += 1
            if idx >= len(n):
                print(num)
                exit(0)
