n = int(input())
sosu = list(map(int, input().split()))
cnt = 0
for i in range(n):
    yaksu = []
    if sosu[i] != 1:
        for j in range(1, sosu[i] + 1):
            if sosu[i] % j == 0:
                yaksu.append(j)
        if len(yaksu) == 2:
            cnt += 1
print(cnt)
