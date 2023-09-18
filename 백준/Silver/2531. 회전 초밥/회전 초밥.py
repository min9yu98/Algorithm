import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
table = [int(input()) for _ in range(n)]
table += table[: (k - 1)]
ans = 0

for i in range(k - 1, len(table)):
    cnt = 0
    tmp = set(table[i - k + 1: i + 1])
    if c not in tmp:
        cnt += 1

    cnt += len(tmp)
    ans = max(ans, cnt)

print(ans)
