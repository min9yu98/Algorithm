import sys

input = sys.stdin.readline

print(str(oct(int(input().strip(), 2)))[2:])
