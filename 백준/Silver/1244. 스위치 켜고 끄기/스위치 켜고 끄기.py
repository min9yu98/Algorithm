n = int(input())
switch = list(map(int, input().split()))
p = int(input())

for _ in range(p):
    gender, loc = map(int, input().split())
    if gender == 1:
        for i in range(1, n // loc + 1):
            if switch[i * loc - 1] == 0:
                switch[i * loc - 1] = 1
            else:
                switch[i * loc - 1] = 0
    else:
        if switch[loc - 1] == 0:
            switch[loc - 1] = 1
        else:
            switch[loc - 1] = 0
        i = loc - 2
        j = loc
        while i >= 0 and j < n:
            if switch[i] == switch[j]:
                if switch[i] == 0:
                    switch[i], switch[j] = 1, 1
                else:
                    switch[i], switch[j] = 0, 0
                i -= 1
                j += 1
            else:
                break


for i in range(n):
    if i % 20 == 0 and i != 0:
        print()
    print(switch[i], end=" ")