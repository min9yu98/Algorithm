import sys


i = 1

while True:
    l, p, v = map(int, input().split())
    if l + p + v == 0:
        break
    d1 = (v // p) * l
    d2 = min(v % p, l)
    print("Case {}: {}".format(i, d1 + d2))
    i += 1
