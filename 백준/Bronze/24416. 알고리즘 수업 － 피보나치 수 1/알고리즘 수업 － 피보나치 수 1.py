fib = [0] * 41
fib[1], fib[2] = 1, 1
n = int(input())
for i in range(3, n + 1):
    fib[i] = fib[i - 1] + fib[i - 2]
print(fib[n], n - 2)
