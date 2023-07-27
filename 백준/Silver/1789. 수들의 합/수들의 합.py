s = int(input())
num = 0
total = 0
cnt = 0

while True:
    num += 1
    total += num
    cnt += 1
    if total > s:
        break

print(cnt - 1)