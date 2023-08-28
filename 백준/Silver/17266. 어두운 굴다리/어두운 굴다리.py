n = int(input())
m = int(input())
loc = list(map(int, input().split()))
distance = [loc[0], n - loc[-1]]

for i in range(m - 1):
    if (loc[i + 1] - loc[i]) % 2 == 0:
        distance.append((loc[i + 1] - loc[i]) // 2)
    else:
        distance.append((loc[i + 1] - loc[i]) // 2 + 1)

print(max(distance))