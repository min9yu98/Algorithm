vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    s = input()
    if s == 'end':
        break

    flag1 = 0
    for i in range(len(s)):
        if s[i] in vowel:
            flag1 = 1
            break
    if flag1 == 0:
        print("<{}> is not acceptable.".format(s))
        continue

    flag2 = 1
    if len(s) >= 3:
        for i in range(len(s) - 2):
            if s[i] in vowel and s[i + 1] in vowel and s[i + 2] in vowel:
                flag2 = 0
                break
            if s[i] not in vowel and s[i + 1] not in vowel and s[i + 2] not in vowel:
                flag2 = 0
                break
    if flag2 == 0:
        print("<{}> is not acceptable.".format(s))
        continue

    flag3 = 1
    if len(s) >= 2:
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                if s[i] == 'e' or s[i] == 'o':
                    continue
                else:
                    flag3 = 0
                    break
    if flag3 == 0:
        print("<{}> is not acceptable.".format(s))
        continue

    if flag1 == 1 and flag2 == 1 and flag3 == 1:
        print("<{}> is acceptable.".format(s))

