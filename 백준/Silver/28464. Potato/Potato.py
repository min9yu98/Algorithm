import sys
input = sys.stdin.readline

n = int(input())
potato = list(map(int, input().split()))
potato.sort()
slice_std = n // 2
print(sum(potato[:slice_std]), sum(potato[slice_std:]))
