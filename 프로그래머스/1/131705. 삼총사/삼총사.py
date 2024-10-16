def solution(number):
    answer = 0
    leng = len(number)
    for i in range(leng):
        for j in range(i + 1, leng):
            for k in range(j + 1, leng):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer