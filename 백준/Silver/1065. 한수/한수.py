n = int(input())
hansu = 0

for i in range(1, n + 1):
    if i < 100:
        hansu += 1
    else:
        x = list(map(int, str(i)))
        if x[0] - x[1] == x[1] - x[2]:
            hansu += 1

print(hansu)
