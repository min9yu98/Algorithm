def solution(k, tangerine):
    answer = 0
    size = len(tangerine)
    type_cnt = len(set(tangerine))
    remove_cnt = size - k
    dic = {}
    for e in tangerine:
        dic[e] = dic.get(e, 0) + 1
    lst = []
    for k, v in dic.items():
        lst.append([k, v])
    lst.sort(key=lambda x: x[1])
    for e in lst:
        if e[1] <= remove_cnt:
            remove_cnt -= e[1]
            type_cnt -= 1
        else:
            break
    return type_cnt