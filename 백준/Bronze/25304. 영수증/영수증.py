import sys


total = int(sys.stdin.readline())

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    total -= n * m

if total == 0:
    sys.stdout.write("Yes")
else:
    sys.stdout.write("No")

