from itertools import permutations
import sys

input = sys.stdin.readline

n = int(input())
having = list(map(int, input().split()))
having.sort()
m = int(input())
numbers = list(map(int, input().split()))

dic = {}
for card in having:
    if card not in dic:
        dic[card] = 1
    else:
        dic[card] += 1

for e in numbers:
    if dic.get(e) == None:
        print(0, end=" ")
    else:
        print(dic.get(e), end=" ")