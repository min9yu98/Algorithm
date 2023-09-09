p, m = map(int, input().split())
room = list()

for _ in range(p):
    l, n = input().split()
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
        print("Started!")
    else:
        print("Waiting!")
    r.sort(key=lambda x: x[1])
    for l, n in r:
        print(l, n)

