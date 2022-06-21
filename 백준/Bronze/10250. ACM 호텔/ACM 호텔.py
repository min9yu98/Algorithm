for _ in range(int(input())):
    h, w, n = map(int, input().split())
    if n % h == 0:
        print(h * 100 + n//h)
    elif n % h != 0:
        print(n % h * 100 + n//h+1)
