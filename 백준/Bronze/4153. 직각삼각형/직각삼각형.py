while True:
    d = sorted(list(map(int, input().split())))
    if d[0] == 0 and d[1] == 0 and d[2] == 0:
        break
    if max(d) ** 2 == d[0] ** 2 + d[1] ** 2:
        print('right')
    else:
        print('wrong')