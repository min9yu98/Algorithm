def solution(n):
    ans = 0
    rem = 0
    while n > 1:
        if n % 2:
            rem += 1
        n //= 2
    ans += rem + n        
    return ans