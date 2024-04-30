import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

for _ in range(int(input())):
    first, second = input().strip().split()
    lst = [0] * 123
    for e in first:
        lst[ord(e)] += 1
    for e in second:
        lst[ord(e)] -= 1
    if lst.count(0) == 123:
        print('Possible')
    else:
        print('Impossible')
