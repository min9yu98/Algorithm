import sys
num = []
for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    num.append([a, b])
num.sort(key = lambda x: (x[0], x[1]))
for n1, n2 in num:
    print(n1, n2)