s = input()
for e in s:
    if 110 <= ord(e) <= 122:
        print(chr((ord(e) + 13) - 122 + 96), end='')
    elif 78 <= ord(e) <= 90:
        print(chr((ord(e) + 13) - 90 + 64), end='')
    elif e == ' ':
        print(' ', end='')
    elif e.isdigit():
        print(e, end='')
    else:
        print(chr(ord(e) + 13), end='')
