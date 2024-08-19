def solution(a, d, included):
    answer = 0
    sequence = [0] * (len(included) + 1)
    for i in range(1, len(included) + 1):
        if i == 1:
            sequence[i] = a
        else:
            sequence[i] = sequence[i - 1] + d
        if included[i - 1]:
            answer += sequence[i]
    return answer