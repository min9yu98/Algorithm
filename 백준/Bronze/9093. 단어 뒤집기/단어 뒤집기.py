import sys
input = sys.stdin.readline

for _ in range(int(input())):
    print(' '.join(list(map(lambda x: x[::-1], input().strip().split()))))
