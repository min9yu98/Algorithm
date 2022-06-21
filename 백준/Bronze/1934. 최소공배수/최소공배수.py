n = int(input())


for i in range(n):
    first, second = map(int, input().split())
    second_li = []
    for j in range(1, second + 1):
        if second % j == 0:
            second_li.append(j)
    first_li = []
    for k in second_li:
        t = first * k
        first_li.append(t)
    sum_ = []
    for l in first_li:
        if l % second == 0:
            sum_.append(l)
    print(min(sum_))