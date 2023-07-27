n = int(input())

for _ in range(n):
    lst = list(map(int, input().split()))
    if lst[0] == lst[1] - lst[2]:
        print("does not matter")
    elif lst[0] < lst[1] - lst[2]:
        print("advertise")
    else:
        print("do not advertise")