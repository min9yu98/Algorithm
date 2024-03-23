import sys

input = sys.stdin.readline

n = int(input())
f = int(input())

start = (n // 100) * 100
end = start + 99

for i in range(start, end + 1):
    if i % f == 0:
        print(str(i)[-2::])
        break
