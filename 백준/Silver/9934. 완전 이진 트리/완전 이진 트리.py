import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

k = int(input())
buildings = list(map(int, input().split()))
ans = [[] for _ in range(k)]


def recur(arr, l):
    ans[l].append(arr[len(arr) // 2])
    if len(arr) == 1:
        return
    recur(arr[:len(arr) // 2], l + 1)
    recur(arr[len(arr) // 2 + 1:], l + 1)


recur(buildings, 0)
for e in ans:
    print(' '.join(map(str, e)))
