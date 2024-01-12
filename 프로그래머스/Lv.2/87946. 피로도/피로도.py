from copy import deepcopy
from itertools import permutations

def solution(k, dungeons):
    answer = []
    tmp = deepcopy(k)
    for comb in list(permutations(dungeons, len(dungeons))):
        cnt = 0
        for e in comb:
            if k >= e[0] and k >= e[1]:
                cnt += 1
                k -= e[1]
            else:
                break
        answer.append(cnt)
        cnt = 0
        k = tmp
    return max(answer)