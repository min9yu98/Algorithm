import sys
_input = sys.stdin.readline

for _ in range(int(_input())):
    s = _input().strip()
    print('{}{}'.format(s[0], s[-1]))
