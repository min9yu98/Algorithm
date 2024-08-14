import sys

input = sys.stdin.readline

N, K = map(int, input().split())
mod = 1000000007


def fact(n):
    x = 1
    for i in range(2, n + 1):
        x = (x * i) % mod
    return x


def square(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    tmp = square(n, k // 2)
    if k % 2:
        return tmp * tmp * n % mod
    else:
        return tmp * tmp % mod


top = fact(N)
bottom = fact(N - K) * fact(K) % mod
print(top * square(bottom, mod - 2) % mod)
