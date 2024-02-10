while True:
    try:
        answer = [0, 0, 0, 0]
        sen = input()
        for s in sen:
            if s.isupper():
                answer[1] += 1
            elif s.islower():
                answer[0] += 1
            elif s.isdigit():
                answer[2] += 1
            else:
                answer[3] += 1
        print(' '.join(list(map(str, answer))))
    except EOFError:
        break