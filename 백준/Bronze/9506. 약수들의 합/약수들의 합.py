while True:
    lst = []
    cnt = 0
    n = int(input())
    if n == -1:
        break
    middle = int(n / 2)
    for i in range(1, middle + 1):
        if n % i == 0:
            cnt += i
            lst.append(i)
    if cnt == n:
        print("{} = ".format(n), end="")
        for i in range(len(lst)):
            print(lst[i], end="")
            if i != len(lst) - 1:
                print(" + ", end="")
            else:
                print()
    else:
        print("{} is NOT perfect.".format(n))