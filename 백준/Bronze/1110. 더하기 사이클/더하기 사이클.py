x = int(input())
num = 0
sum1 = 0
sum2 = x
while True:
    ten = sum2 // 10
    one = sum2 % 10
    sum1 = ten + one
    sum1 = one * 10 + (sum1 % 10)
    num += 1
    sum2 = sum1
    if sum2 == x:
        break
print(num)