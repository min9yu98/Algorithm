import sys
input = sys.stdin.readline

num = list(input().strip())
num.sort(reverse=True)
answer = 0
if '0' not in num:
    print(-1)
    exit(0)
else:
    cnt = 0
    for e in num:
        cnt += int(e)
    if cnt % 3 == 0:
        print(''.join(num))
    else:
        print(-1)
