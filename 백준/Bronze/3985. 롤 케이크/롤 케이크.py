import sys

input = sys.stdin.readline

l = int(input())
n = int(input())

maxi = 0
expect_lst = []
cakes = [0] * (l + 1)
maxi = 0
idx = 0
for i in range(1, n + 1):
    a, b = map(int, input().split())
    cnt = 0
    for j in range(a, b + 1):
        if cakes[j] == 0:
            cakes[j] = i
            cnt += 1
    if maxi < cnt:
        maxi = cnt
        idx = i
    expect_lst.append([i, (b - a + 1)])
expect_lst.sort(key=lambda x: -x[1])
print(expect_lst[0][0])
print(idx)