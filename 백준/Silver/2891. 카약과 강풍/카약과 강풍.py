import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n, s, r = map(int, input().split())
problem = list(map(int, input().split()))
more = list(map(int, input().split()))
boat = [1] * (n + 1)
for b in problem:
    boat[b] -= 1
for b in more:
    boat[b] += 1
for i in range(1, n + 1):
    if boat[i] == 0:
        if i == 1:
            if boat[i + 1] > 1:
                boat[i] += 1
                boat[i + 1] -= 1
        elif i == n:
            if boat[i - 1] > 1:
                boat[i] += 1
                boat[i - 1] -= 1
        else:
            if boat[i - 1] > 1:
                boat[i - 1] -= 1
                boat[i] += 1
                continue
            if boat[i + 1] > 1:
                boat[i + 1] -= 1
                boat[i] += 1
                continue
print(boat.count(0))
