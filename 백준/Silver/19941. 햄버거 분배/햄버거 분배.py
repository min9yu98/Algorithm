n, k = map(int, input().split())
lst = list(map(str, input()))
cnt = 0
for i in range(n):
    if lst[i] == 'P':
        for j in range(max(i - k, 0), min(n, i + k + 1)):
            if lst[j] == 'H':
                cnt += 1
                lst[j] = 0
                break
print(cnt)
