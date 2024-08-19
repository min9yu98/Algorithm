def solution(price, money, count):
    answer = 0
    total = 0
    for i in range(1, count + 1):
        total += price * i
    return answer if total <= money else total - money