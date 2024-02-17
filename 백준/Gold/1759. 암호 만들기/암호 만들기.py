from itertools import combinations

l, c = map(int, input().split())
words = input().split()
words.sort()
comb = list(combinations(words, l))
for word in comb:
    a = word.count('a')
    e = word.count('e')
    i = word.count('i')
    o = word.count('o')
    u = word.count('u')
    total = a + e + i + o + u
    if a + e + i + o + u != 0 and len(word) - total >= 2:
        print(''.join(word))
