n, d = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
road = [i for i in range(d + 1)]

for i in range(d + 1):
    road[i] = min(road[i], road[i - 1] + 1)
    for start, end, short in lst:
        if i == start and end <= d:
            road[end] = min(road[end], road[i] + short)

print(road[-1])
