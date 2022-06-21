for _ in range(int(input())):
    x = list(map(int, input().split()))
    total_point = cnt = 0
    for i in range(1, len(x)):
        total_point += x[i]
    average_point = total_point / x[0]
    for i in range(1, len(x)):
        if x[i] > average_point:
            cnt += 1
    per = round((cnt / x[0]) * 100, 3)
    print('%0.3f'%per, '%', sep = '')
