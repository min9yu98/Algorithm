import sys

input = sys.stdin.readline

n = int(input())
student_numbers = list(map(int, input().split()))
order = [1]
for i in range(1, n):
    order.insert(i - student_numbers[i], i + 1)
for e in order:
    print(e, end=' ')
