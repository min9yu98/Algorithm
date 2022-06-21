h, m = map(int, input().split())
result = h * 60 + m - 45
if result < 0:
    print((24 * 60 + result)//60, (24 * 60 + result)%60)
else:
    print(result//60, result%60)
