import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p_price = []
e_price = []
for _ in range(m):
    p, e = map(int, input().split())
    p_price.append(p)
    e_price.append(e)
p_price.sort()
e_price.sort()
if n <= 6:
    print(min(p_price[0], e_price[0] * n))
else:
    stand = n // 6 + 1  # -> 15 : 3
    mini = stand * p_price[0]
    for i in range(stand):
        price = p_price[0] * i + e_price[0] * (n - (i * 6))
        if mini > price:
            mini = price
    print(mini)

