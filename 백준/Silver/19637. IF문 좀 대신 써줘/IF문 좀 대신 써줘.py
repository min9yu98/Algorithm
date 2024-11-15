import sys

input = sys.stdin.readline

n, m = map(int, input().split())
name_lst = []
power_lst = []
for _ in range(n):
    name, power = input().strip().split()
    name_lst.append(name)
    power_lst.append(int(power))


def binary_search(score):
    start, end = 0, len(power_lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if score > power_lst[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return name_lst[start]


for _ in range(m):
    sc = int(input())
    print(binary_search(sc))