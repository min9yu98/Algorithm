import sys
input = sys.stdin.readline

n = int(input())

loop = n // 5
result = -1
for i in range(loop + 1):
    bal = (n - (5 * (loop - i)))
    if bal % 2 == 0:
        result = (loop - i) + ((n - (5 * (loop - i))) // 2)
        break
print(result)
