while True:
    s = input().lower()
    if s == '#':
        break
    answer = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')
    print(answer)
