import sys


exp = input().split("-")
num = []

for i in exp:
    total = 0
    total += sum(map(int, i.split("+")))
    num.append(total)

result = num[0]
for i in range(1, len(num)):
    result -= num[i]

print(result)