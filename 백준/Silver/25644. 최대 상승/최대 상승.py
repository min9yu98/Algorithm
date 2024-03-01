import sys
input = sys.stdin.readline

n = int(input())
stocks = list(map(int, input().split()))
benefit, result = 0, 0
for i in range(n - 1, -1, -1):
    benefit = max(benefit, stocks[i])
    result = max(result, benefit - stocks[i])
print(result)
