import sys
input = sys.stdin.readline

numbers = input().strip()
one, zero = 0, 0
if numbers[0] == '0':
    zero += 1
elif numbers[0] == '1':
    one += 1
for i in range(len(numbers) - 1):
    if numbers[i] != numbers[i + 1]:
        if numbers[i] == '0':
            one += 1
        elif numbers[i] == '1':
            zero += 1
print(min(zero, one))
