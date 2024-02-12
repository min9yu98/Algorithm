n, m = map(int, input().split())
fish = [list(reversed(list(input()))) for _ in range(n)]
for i in range(n):
    print(''.join(fish[i]))
