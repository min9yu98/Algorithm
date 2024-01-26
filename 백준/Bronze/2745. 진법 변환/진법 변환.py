n, b = input().split()
b = int(b)
result = 0
for i in range(len(n)):
    if n[i].isdigit():
        result += int(n[i]) * (b ** (len(n) - 1 - i))
    else:
        result += (ord(n[i]) - 55) * (b ** (len(n) - 1 - i))
print(result)
