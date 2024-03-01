import sys
input = sys.stdin.readline

n = int(input())
doll = list(map(int, input().split()))
for i in range(len(doll)):
    if doll[i] != 0:
        rep = [doll[i]]
        for j in range(i + 1, len(doll)):
            if doll[j] != 0 and doll[j] not in rep:
                rep.append(doll[j])
                doll[j] = 0
        n = n - (len(rep) - 1)
print(n)
