s = input()
length = 10
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        length += 10
    else:
        length += 5
print(length)