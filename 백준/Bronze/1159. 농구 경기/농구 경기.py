import sys

input = sys.stdin.readline

alpha = {chr(i): 0 for i in range(97, 123)}
n = int(input())
for _ in range(n):
    player = input().strip()
    alpha[player[0]] += 1

flag = False
for key, value in alpha.items():
    if value >= 5:
        flag = True
        print(key, end="")
if not flag:
    print("PREDAJA")
