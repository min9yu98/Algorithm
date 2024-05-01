import sys

input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    pwd = []
    mv = []
    point = 0
    for e in s:
        if e == '<':
            if pwd:
                mv.append(pwd.pop())
        elif e == '>':
            if mv:
                pwd.append(mv.pop())
        elif e == '-':
            if pwd:
                pwd.pop()
        else:
            pwd.append(e)

    print("".join(pwd), "".join(mv[::-1]), sep="")
