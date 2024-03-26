import sys

input = sys.stdin.readline

n, k = map(int, input().split())
boy, girl = {i: 0 for i in range(1, 7)}, {i: 0 for i in range(1, 7)}
total = 0
for _ in range(n):
    gender, grade = map(int, input().split())
    if gender:
        boy[grade] += 1
    else:
        girl[grade] += 1
total = 0
for b, g in zip(boy.values(), girl.values()):
    total += b // k + g // k
    if b % k:
        total += 1
    if g % k:
        total += 1
print(total)
