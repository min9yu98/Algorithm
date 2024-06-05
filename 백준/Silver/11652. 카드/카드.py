import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
s = set(arr)
dic = {}
for x in s:
    dic[x] = 0
arr.sort()
for i in range(n):
    dic[arr[i]] += 1
print(sorted(dic.items(), key=lambda x: (x[1], -x[0]), reverse=True)[0][0])
