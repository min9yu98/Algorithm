graph = [list(map(int, input().split())) for _ in range(9)]

max_x, max_y = 0, 0
maxi = 0
for i in range(9):
    for j in range(9):
        if maxi < graph[i][j]:
            maxi = graph[i][j]
            max_x = i
            max_y = j
print(maxi)
print(max_x + 1, max_y + 1)
