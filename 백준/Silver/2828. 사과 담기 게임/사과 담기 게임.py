import sys
input = sys.stdin.readline

n, m = map(int, input().split())
apple_cnt = int(input())
now = 1
basket = [int(input()) for _ in range(apple_cnt)]
result = 0
for apple in basket:
    if now <= apple <= now + (m - 1):
        pass
    elif now > apple:
        result += abs(apple - now)
        now = apple
    else:
        result += apple - (m - 1) - now
        now = apple - (m - 1)
print(result)