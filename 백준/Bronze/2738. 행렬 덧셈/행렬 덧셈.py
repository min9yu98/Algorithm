import sys


x, y = map(int, input().split())
lst1, lst2 = [], []

for _ in range(x):
    lst1.append(list(map(int, input().split())))

for _ in range(x):
    lst2.append(list(map(int, input().split())))

for j in range(x):
    for i in range(y):
        print(lst1[j][i] + lst2[j][i], end=" ")
    print()
