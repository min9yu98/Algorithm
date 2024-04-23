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


def binary(arr, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    if arr[mid] == target:
        return dic.get(target)
    elif arr[mid] < target:
        return binary(arr, target, mid + 1, end)
    elif arr[mid] > target:
        return binary(arr, target, start, mid - 1)


for target in numbers:
    print(binary(having, target, 0, n - 1), end=" ")
