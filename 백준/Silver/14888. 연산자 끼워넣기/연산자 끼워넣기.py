import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
operand = list(map(int, input().split()))

maxi = -1e9
mini = 1e9


def back(idx, total, plus, minus, multiply, divide):
    global maxi, mini
    if idx == n:
        maxi = max(total, maxi)
        mini = min(total, mini)
    if plus:
        back(idx + 1, total + numbers[idx], plus - 1, minus, multiply, divide)
    if minus:
        back(idx + 1, total - numbers[idx], plus, minus - 1, multiply, divide)
    if multiply:
        back(idx + 1, total * numbers[idx], plus, minus, multiply - 1, divide)
    if divide:
        back(idx + 1, int(total / numbers[idx]), plus, minus, multiply, divide - 1)


back(1, numbers[0], operand[0], operand[1], operand[2], operand[3])
print(maxi)
print(mini)
