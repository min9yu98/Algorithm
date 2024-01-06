import sys
input = sys.stdin.readline

numbers = input().strip()
cnt = 0
for i in range(len(numbers) - 1):
    if numbers[i] != numbers[i + 1]:
        cnt += 1
print((cnt + 1) // 2)
