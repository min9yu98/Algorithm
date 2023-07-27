n = int(input())

for _ in range(n):
    s = input().split()
    if s[0].isnumeric():
        num = int(s[0])
    else:
        num = float(s[0])
    for i in range(1, len(s)):
        if ord(s[i]) == 64:
            num *= 3
        elif ord(s[i]) == 37:
            num += 5
        else:
            num -= 7
    print("{0:.2f}".format(float(num)))