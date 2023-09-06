import sys

input = sys.stdin.readline

N, M = map(int, input().split())
power_lst = []
name_lst = []
for i in range(N):
    stand, stand_score = input().split()
    power_lst.append(int(stand_score))
    name_lst.append(stand)


def binary_search(score):
    left = 0
    right = len(power_lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if score > power_lst[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return name_lst[right + 1]


for _ in range(M):
    score = int(input())
    print(binary_search(score))
