import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a = list(map(int, input().split()))[1:]
    b = list(map(int, input().split()))[1:]
    a_check = [0] * 5
    b_check = [0] * 5

    flag = False
    for i in range(4, 0, -1):
        if a.count(i) > b.count(i):
            print('A')
            flag = True
            break
        elif a.count(i) < b.count(i):
            print('B')
            flag = True
            break
    if not flag:
        print('D')

