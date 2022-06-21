i = list(map(int, input().split()))
card = i[0]
total = i[1]
lst = list(map(int, input().split()))
answer = []
for i in range(len(lst) - 2):
    for j in range(i + 1, len(lst) - 1):
        for k in range(j + 1, len(lst)):
            if (total - (lst[i] + lst[j] + lst[k])) >= 0:
                answer.append(lst[i] + lst[j] + lst[k])

print(max(answer))
