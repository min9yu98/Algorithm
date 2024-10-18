def solution(k, score):
    answer = []
    lst = []
    for s in score:
        if len(lst) < k:
            lst.append(s)
            answer.append(min(lst))
        else:
            mini = min(lst)
            if mini < s:
                lst.remove(mini)
                lst.append(s)
            answer.append(min(lst))
    return answer