n = [list(map(int, input().split())) for _ in range(3)]
x = []
y = []
for a, b in n:
    x.append(a)
    y.append(b)
for i in range(3):
    if x.count(x[i]) == 1:
        result_x = x[i]
    if y.count(y[i]) == 1:
        result_y = y[i]
print(result_x, result_y)
