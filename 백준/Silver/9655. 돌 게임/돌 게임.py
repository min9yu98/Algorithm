n = int(input())

flag = n // 3 + n % 3

print('SK' if flag % 2 else 'CY')