import sys

word = list(sys.stdin.readline().rstrip())
word_tmp = []
for _ in range(int(sys.stdin.readline())):
    com = list(sys.stdin.readline().rstrip().split())
    if com[0] == 'P':
        word.append(com[1])
    elif com[0] == 'D':
        if word_tmp:
            word.append(word_tmp.pop())
    elif com[0] == 'L':
        if word:
            word_tmp.append(word.pop())
    elif com[0] == 'B':
        if word:
            word.pop()
word.extend(reversed(word_tmp))
print(''.join(word))
