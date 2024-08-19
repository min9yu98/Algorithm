def solution(name, yearning, photo):
    answer = []
    score = {n: y for n, y in zip(name, yearning)}
    for lst in photo:
        s = 0
        for p in lst:
            if p in name:
                s += score[p]
        answer.append(s)
    return answer