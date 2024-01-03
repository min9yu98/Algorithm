import sys
import math
_input = sys.stdin.readline

n, k = map(int, _input().split())

if n == k or k == 0:
    print(1)
    exit(0)
mo = math.factorial(n)
so = math.factorial(n - k) * math.factorial(k)

print(int(mo / so))
