import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

for _ in range(m):
    numbers[0] = numbers[0] + numbers[1]
    numbers[1] = numbers[0]
    numbers.sort()
print(sum(numbers))
