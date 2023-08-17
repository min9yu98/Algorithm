p = int(input())

for _ in range(p):
    member = list(map(int, input().split()))
    cnt = 0
    for i in range(1, len(member) - 1):
        for j in range(i + 1, len(member)):
            if member[i] > member[j]:
                member[i], member[j] = member[j], member[i]
                cnt += 1
    print(member[0], cnt)
