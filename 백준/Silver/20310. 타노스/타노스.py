lst = list(input())
zero = lst.count('0') // 2
one = lst.count('1') // 2
for _ in range(zero):
    lst.pop(-(lst[::-1].index('0')) - 1)
for _ in range(one):
    lst.pop(lst.index('1'))
print(''.join(lst))
