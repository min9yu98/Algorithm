fact = [0] * 21
fact[0] = 1
for i in range(1, 21):
    cnt = 1
    for j in range(1, i + 1):
        cnt *= j
    fact[i] = cnt
n = int(input())
if n == 0:
    print('NO')
else:
    for i in range(20, -1, -1):
        if fact[i] <= n:
            n -= fact[i]
    print('YES') if n == 0 else print('NO')