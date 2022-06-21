a = int(input())
b = input()

for i in reversed(range(len(b))):
    print(a * int(b[i]))
print(a * int(b))
