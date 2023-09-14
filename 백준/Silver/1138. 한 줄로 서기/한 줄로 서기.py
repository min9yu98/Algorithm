n = int(input())
num_lst = [0] + list(map(int, input().split()))
ans = [0] * n

for i in range(1, n + 1):
    cnt = 0
    tmp = num_lst[i]
    for j in range(n):
        if ans[j] == 0 and cnt == tmp:
            ans[j] = i
            break
        elif ans[j] == 0:
            cnt += 1
print(" ".join(map(str, ans)))
