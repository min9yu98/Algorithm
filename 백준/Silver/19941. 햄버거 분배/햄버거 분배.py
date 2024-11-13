import sys

input = sys.stdin.readline

n, k = map(int, input().split())
choice = list(input().strip())
cnt = 0
for i in range(n):
    if choice[i] == 'P':
        for j in range(max(i - k, 0), min(n, i + k + 1)):
            if choice[j] == 'H':
                cnt += 1
                choice[j] = 'O'
                break
print(cnt)