warehouses = []
total = 0
n = int(input())

for _ in range(n):
    l, h = map(int, input().split())
    warehouses.append((l, h))
warehouses.sort()

max_h_idx = 0
for i in range(n):
    if total < warehouses[i][1]:
        total = warehouses[i][1]
        max_h_idx = i

h = warehouses[0][1]
for i in range(max_h_idx):
    if h < warehouses[i + 1][1]:
        total += (warehouses[i + 1][0] - warehouses[i][0]) * h
        h = warehouses[i + 1][1]
    else:
        total += (warehouses[i + 1][0] - warehouses[i][0]) * h

h = warehouses[-1][1]
for i in range(n - 1, max_h_idx, -1):
    if h < warehouses[i - 1][1]:
        total += (warehouses[i][0] - warehouses[i - 1][0]) * h
        h = warehouses[i - 1][1]
    else:
        total += (warehouses[i][0] - warehouses[i - 1][0]) * h

print(total)
