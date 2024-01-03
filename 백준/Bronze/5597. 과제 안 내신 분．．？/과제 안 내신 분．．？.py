import sys
_input = sys.stdin.readline

numbers = [0 for _ in range(31)]
numbers[0] = 1
for _ in range(28):
    idx = int(_input())
    numbers[idx] = 1
result = list(filter(lambda e: numbers[e] == 0, range(31)))
print(result[0])
print(result[1])
