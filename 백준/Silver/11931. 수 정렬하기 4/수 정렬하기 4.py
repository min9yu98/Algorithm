import sys

input = sys.stdin.readline

for e in sorted([int(input()) for _ in range(int(input()))], reverse=True): print(e)
