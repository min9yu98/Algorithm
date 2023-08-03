for _ in range(int(input())):
    lst = []
    for _ in range(int(input())):
        name, num = input().split()
        num = int(num)
        lst.append([name, num])
    lst = sorted(lst, key=lambda x: x[1])
    print(lst[-1][0])