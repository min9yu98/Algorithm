import sys

input = sys.stdin.readline

while True:
    try:
        s, t = input().strip().split()
        flag = False
        idx = 0
        for w in t:
            if w == s[idx]:
                idx += 1
                if len(s) == idx:
                    flag = True
                    break
        if flag:
            print('Yes')
        else:
            print('No')
    except:
        break
