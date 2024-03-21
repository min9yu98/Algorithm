import sys

input = sys.stdin.readline

n = int(input())
taker = list(map(int, input().split()))
b, c = map(int, input().split())

total = 0
for e in taker:
    total += 1
    e -= b
    if e >= 0:
        total += e // c
        if e % c:
            total += 1
print(total)

