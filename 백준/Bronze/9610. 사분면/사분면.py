n = int(input())
cnt = [0, 0, 0, 0, 0]

for _ in range(n):
    a, b = map(int, input().split())
    if a == 0 or b == 0:
        cnt[0] += 1
    elif a > 0 and b > 0:
        cnt[1] += 1
    elif a < 0 < b:
        cnt[2] += 1
    elif a < 0 and b < 0:
        cnt[3] += 1
    elif a > 0 > b:
        cnt[4] += 1

print("Q1: {}".format(cnt[1]))
print("Q2: {}".format(cnt[2]))
print("Q3: {}".format(cnt[3]))
print("Q4: {}".format(cnt[4]))
print("AXIS: {}".format(cnt[0]))