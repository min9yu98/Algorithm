import sys


lst = [sys.stdin.readline().rstrip('\n') for _ in range(36)]
check = [[0 for _ in range(6)] for _ in range(6)]
state = "Valid"

if abs(ord(lst[0][0]) - ord(lst[-1][0])) == 1 and abs(int(lst[0][1]) - int(lst[-1][1])) == 2 \
        or abs(ord(lst[0][0]) - ord(lst[-1][0])) == 2 and abs(int(lst[0][1]) - int(lst[-1][1])) == 1:
    for i in range(1, len(lst)):
        check1 = abs(ord(lst[i][0]) - ord(lst[i - 1][0]))
        check2 = abs(int(lst[i][1]) - int(lst[i - 1][1]))
        nlx, nly = ord(lst[i][0]) - 65, int(lst[i][1]) - 1
        if check1 == 1 and check2 == 2 or check1 == 2 and check2 == 1:
            check[nlx][nly] += 1

            if check[nlx][nly] != 1:
                state = "Invalid"
                break
        else:
            state = "Invalid"
            break
else:
    state = "Invalid"

print(state)
