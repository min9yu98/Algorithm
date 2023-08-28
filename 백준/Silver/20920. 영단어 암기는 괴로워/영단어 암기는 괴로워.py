import sys

n, m = map(int, sys.stdin.readline().split())
dic = {}

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if len(word) < m:
        continue
    if word in dic.keys():
        dic[word] += 1
    else:
        dic[word] = 1

result = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for e in result:
    print(e[0])
