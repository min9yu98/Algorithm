import sys
input = sys.stdin.readline

s = input().strip()

tmp = ''
dot = ''
lst = []
for i in range(len(s)):
    if s[i] != '.':  # s[i] == 'X'
        tmp += s[i]
        if dot != '':
            lst.append(dot)
            dot = ''
    else:
        dot += s[i]
        if tmp != '':
            lst.append(tmp)
            tmp = ''
if tmp != '':
    lst.append(tmp)
if dot != '':
    lst.append(dot)
p = []
for e in lst:
    if len(e) % 2 != 0 and e[0] != '.':
        print(-1)
        exit()
    if e[0] != '.':
        if len(e) >= 4:
            if len(e) % 4 == 0:
                p.append('AAAA' * (len(e) // 4))
            else:
                p.append(('AAAA' * (len(e) // 4)) + ('BB' * ((len(e) % 4) // 2)))
        else:
            p.append('BB')
    else:
        p.append(e)
answer = ''.join(p)
print(answer)
