from itertools import permutations
import sys

input = sys.stdin.readline

a, b = map(int, input().split())
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

a_set = set(a_arr)
b_set = set(b_arr)
ans_set = a_set.difference(b_set)
ans = sorted(list(ans_set))
print(len(ans))
print(' '.join(map(str, ans)))
