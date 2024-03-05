import sys
input = sys.stdin.readline

n = int(input())
atn = list(map(int, input().split()))
atn.sort()
print(atn[(n - 1) // 2])
