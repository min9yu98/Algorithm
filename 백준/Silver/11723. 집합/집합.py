import sys

m = int(sys.stdin.readline())
lst = [0] * 21

for _ in range(m):
    temp = sys.stdin.readline().strip().split()

    if len(temp) == 1:
        if temp[0] == "all":
            lst = [1] * 21
            lst[0] = 0
        else:
            lst = [0] * 21

    else:
        func, x = temp[0], temp[1]
        x = int(x)

        if func == "add":
            lst[x] = 1
        elif func == "remove":
            lst[x] = 0
        elif func == "check":
            if lst[x] != 0:
                print(1)
            else:
                print(0)
        elif func == "toggle":
            if lst[x] != 0:
                lst[x] = 0
            else:
                lst[x] = 1
