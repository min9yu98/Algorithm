import sys

input = sys.stdin.readline

p, m = map(int, input().split())
room = []
for _ in range(p):
    l, n = input().strip().split()
    l = int(l)
    flag = False
    for r in room:
        if len(r) < m and abs(l - r[0][0]) <= 10:
            r.append((l, n))
            flag = True
            break
    if not flag:
        room.append([(l, n)])

for r in room:
    if len(r) == m:
        print('Started!')
    else:
        print('Waiting!')
    r.sort(key=lambda x: x[1])
    for e in r:
        print(e[0], e[1])
