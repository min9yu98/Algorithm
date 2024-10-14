def solution(A,B):
    lst1 = sorted(A)
    lst2 = sorted(B, reverse=True)
    answer = 0
    for x, y in zip(lst1, lst2):
        answer += x * y
    
    return answer