def solution(targets):
    targets = sorted(targets, key=lambda x: (x[1], x[0]))
    
    cur, answer = 0, 0
    for i in range(len(targets)):
        if cur > targets[i][0]:
            continue
        cur = targets[i][1]
        answer += 1
    
    return answer

