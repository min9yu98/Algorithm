n = int(input())
three = n // 3
one = n % 3
if (three + one) % 2 == 0:
    print('SK')
else:
    print('CY')
