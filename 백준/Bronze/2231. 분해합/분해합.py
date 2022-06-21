n = int(input())
num = 0
for i in range(1, n + 1):
    div_num = list(map(int, str(i)))
    sum_num = i + sum(div_num)
    if sum_num == n:
        num = i
        break
print(num)

