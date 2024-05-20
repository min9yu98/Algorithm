import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))


def back(rep):
    if len(rep) == m:
        print(' '.join(map(str, rep)))
        return
    for i in range(n):
        rep.append(arr[i])
        back(rep)
        rep.pop()

back([])
