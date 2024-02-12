a, b = map(int, input().split())
c = int(input())
total = a + b
if c * 2 <= total:
    print(total - c * 2)
else:
    print(total)
