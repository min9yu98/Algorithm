n, k = map(int, input().split())
lst = list(map(int, input().split()))
x, y = 0, 0
check_lst = [0] * (max(lst) + 1)
ans = 0

while y < n:
    if check_lst[lst[y]] < k:
        check_lst[lst[y]] += 1
        y += 1
    else:
        check_lst[lst[x]] -= 1
        x += 1
    ans = max(ans, y - x)
print(ans)
