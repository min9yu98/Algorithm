n = list(map(int, input().split()))
n_set = sorted(set(n))
if len(n_set) == 3:
    print(max(n_set) * 100)
elif len(n_set) == 2:
    for i in n_set:
        if n.count(i) == 2:
            print(i * 100 + 1000)
elif len(n_set) == 1:
    print(n_set[0] * 1000 + 10000)
