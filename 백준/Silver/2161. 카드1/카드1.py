import sys

input = sys.stdin.readline

lst = [i for i in range(1, int(input()) + 1)]
while lst:
    print(lst[0], end=' ')
    lst.remove(lst[0])
    if not lst:
        break
    lst.append(lst[0])
    lst.remove(lst[0])