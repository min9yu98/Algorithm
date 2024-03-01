import sys
input = sys.stdin.readline

p, n = map(int, input().split())
equip = list(map(int, input().split()))
equip.sort()
cnt = 0
for t in equip:
    if p < 200:
        p += t
        cnt += 1
print(cnt)
