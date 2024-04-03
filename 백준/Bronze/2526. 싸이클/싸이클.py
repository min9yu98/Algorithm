import sys

input = sys.stdin.readline

n, p = map(int, input().split())
N = n

check = []

while True:
    n = (N * n) % p
    if n in check:
        print(len(check) - check.index(n))
        break
    check.append(n)
