import sys


a, b, c = map(int, sys.stdin.readline().split())

for _ in range(c):
    a = (a % b) * 10
    result = a // b

print(result)




