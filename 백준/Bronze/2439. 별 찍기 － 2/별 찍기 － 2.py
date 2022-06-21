floor = int(input())
for i in range(floor, 0, -1):
    for j in range(1, floor+1):
        if j == i :
            print(' '*(j-1) + '*'*((floor-j)+1), end = '')
    print()