n = int(input())
stand = list(input())
cnt = 0

for _ in range(n - 1):
    stand_copy = stand.copy()
    word = list(input())
    tmp = 0
    for w in word:
        if w in stand_copy:
            stand_copy.remove(w)
        else:
            tmp += 1
    if tmp < 2 and len(stand_copy) < 2:
        cnt += 1
print(cnt)