n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))
total = 0
tmp = 0

i = 0
j = 1
while j < n:
    if cost[i] > cost[j]:
        if j == n - 1:
            tmp += distance[j - 1]
        if tmp == 0:
            total += cost[i] * distance[i]
        else:
            total += cost[i] * tmp
            tmp = 0
        i += j
        j += 1
    else:
        tmp += distance[j - 1]
        j += 1

if tmp != 0:
    total += cost[i] * tmp
print(total)