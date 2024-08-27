def solution(today, terms, privacies):
    result = []
    today = list(map(int, today.split('.')))
    dic = {}
    for e in terms:
        tmp = e.split()
        dic[tmp[0]] = int(tmp[1])
    for i in range(len(privacies)):
        start, terms_type = privacies[i].split()
        start = list(map(int, start.split('.')))
        tmp = dic[terms_type]
        start[0] += tmp // 12
        start[1] += tmp % 12
        if start[1] > 12:
            start[0] += start[1] // 12
            start[1] = start[1] % 12 if start[1] % 12 else 12
        if start[0] > today[0]:
            continue
        elif start[0] == today[0]:
            if start[1] > today[1]:
                continue
            elif start[1] == today[1]:
                if start[2] > today[2]:
                    continue
        result.append(i + 1)
    return result
    