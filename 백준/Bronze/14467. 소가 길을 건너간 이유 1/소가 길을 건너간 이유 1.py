import sys

input = sys.stdin.readline

n = int(input())
cow_status = [0] * (n + 1)
cow_check = [0] * (n + 1)
cnt = 0
for _ in range(n):
    c, d = map(int, input().split())
    if cow_check[c] != 0 and cow_status[c] != d:
        cnt += 1
    cow_check[c] = 1
    cow_status[c] = d
print(cnt)
