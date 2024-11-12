n = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

ans = 0
cost = costs[0]
for i in range(n - 1):
    if cost > costs[i]:
        cost = costs[i]
    ans += cost * roads[i]
print(ans)
