for _ in range(int(input())):
    x = int(input())
    print("{0} {1} {2} {3}".format(x // 25, (x % 25) // 10, ((x % 25) % 10) // 5, ((x % 25) % 10) % 5))
