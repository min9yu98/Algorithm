import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

n, m = map(int, input().split())
process = [list(map(int, input().split())) for _ in range(2)]


def recur(day, place, mission, total):
    if day == 0:
        if total >= m:
            return 1
        else:
            return 0
    ans = 0
    for mi in range(2):  # mission
        for p in range(3):  # place
            if place == p:
                ans += recur(day - 1, p, mi, total + (process[mi][p] / 2))
            else:
                ans += recur(day - 1, p, m, total + process[mi][p])
    return ans


print(recur(n, -1, -1, 0))
