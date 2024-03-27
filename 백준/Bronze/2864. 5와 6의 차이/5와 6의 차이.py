import sys

input = sys.stdin.readline

a, b = map(str, input().strip().split())

print(int(a.replace("6", "5")) + int(b.replace("6", "5")), int(a.replace("5", "6")) + int(b.replace("5", "6")))
