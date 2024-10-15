def solution(s):
    answer = []
    lst = s.lower().split(' ')
    for word in lst:
        if word:
            answer.append(word[0].upper() + word[1:])
        else:
            answer.append(word)
    return ' '.join(answer)