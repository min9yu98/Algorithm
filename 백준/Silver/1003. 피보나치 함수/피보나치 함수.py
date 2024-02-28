import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    if n == 0:
        print(1, 0)
        continue
    fib = [0 for _ in range(n + 1)]
    fib[1] = 1
    if n > 1:
        fib[2] = 1
    for i in range(2, n+1):
        fib[i] = fib[i - 1] + fib[i - 2]
    print(fib[n - 1], fib[n])
