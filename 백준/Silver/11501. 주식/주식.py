for _ in range(int(input())):
    day = int(input())
    stocks = list(map(int, input().split()))
    stocks.reverse()

    max = stocks[0]
    total = 0
    for s in stocks:
        if max < s:
            max = s
            continue
        total += max - s
    print(total)