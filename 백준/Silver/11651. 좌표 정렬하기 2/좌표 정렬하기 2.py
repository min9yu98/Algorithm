location = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    location.append([x, y])
for x, y in sorted(location, key = lambda x: (x[1], x[0])):
    print(x, y)