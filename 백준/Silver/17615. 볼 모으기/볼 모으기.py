n = int(input())
s = input()
cnt_lst = []

rex_R = s.rstrip('R')
cnt_lst.append(rex_R.count('R'))

rex_B = s.rstrip('B')
cnt_lst.append(rex_B.count('B'))

lex_R = s.lstrip('R')
cnt_lst.append(lex_R.count('R'))

lex_B = s.lstrip('B')
cnt_lst.append(lex_B.count('B'))

print(min(cnt_lst))
