n = int(input())
flag = n % 2 == 0
for i in range(n):
    if flag:
        print('* ' * (n // 2), end='')
    else:
        print('* ' * (n // 2 + 1), end='')
    print()
    print(' *' * (n // 2))
