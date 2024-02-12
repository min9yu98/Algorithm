while True:
    s = input()
    if s == '# 0 0':
        break
    s = s.split()
    if 17 < int(s[1]) or 80 <= int(s[2]):
        print('{} {}'.format(s[0], 'Senior'))
    else:
        print('{} {}'.format(s[0], 'Junior'))