import sys

input = sys.stdin.readline

n = int(input())
s = set()
for _ in range(n):
    name, status = map(str, input().strip().split())
    if status == 'enter':
        s.add(name)
    elif status == 'leave':
        s.remove(name)
in_comp = list(s)
in_comp.sort(reverse=True)
for e in in_comp:
    print(e)
