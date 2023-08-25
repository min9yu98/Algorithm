n, k = map(int, input().split())
lst = [[0, 0, 0, 0] for _ in range(n + 1)]
rank = 1
tmp = 1
for _ in range(n):
    a, b, c, d = map(int, input().split())
    lst[a][0] = a
    lst[a][1] = b
    lst[a][2] = c
    lst[a][3] = d
lst.sort(key=lambda x: (x[1], x[2], x[3]))

for i in range(n, 0, -1):
    if lst[i][0] == k:
        print(rank)
        break
    if lst[i][1] == lst[i - 1][1] and lst[i][2] == lst[i - 1][2] and lst[i][3] == lst[i - 1][3]:
        tmp += 1
        continue
    rank += tmp
    tmp = 1
